from django.shortcuts import render
from django.http import FileResponse, HttpResponseNotFound
import stepic
from PIL import Image # importing the Image module from the PIL library.
import io

# Create your views here.

def index(request):
    return render(request, 'index.html')


def hide_text_in_image(image, text):
    data = text.encode('utf-8')
    '''encode('utf-8') on a string, it translates the human-readable 
    characters into a sequence of bytes using the UTF-8 encoding.
     The result is a bytes object in Python.'''
    return stepic.encode(image, data)
#stepic.encode method is called to hide these bytes within the image



def encryption_view(request):
    message = ''
    if request.method == 'POST':
        text = request.POST['text']
        image_file = request.FILES['image']
        image = Image.open(image_file)

        # Convert to PNG if not already in that format
        if image.format != 'PNG':  # checks whether the image format is not PNG.
            image = image.convert('RGBA')
            # image is converted to RGBA mode if it's not already
            # This ensures the image has the correct color channels.
            buffer = io.BytesIO()
            # A BytesIO object is created,
            # which is a binary stream (an in-memory bytes buffer).
            image.save(buffer, format="PNG")
            image = Image.open(buffer)

        # hide text in image
        new_image = hide_text_in_image(image, text)

        # save the new image in a project folder
        image_path = 'project_folder/encrypted_images/' + 'Encrp_' + image_file.name
        
        # Store image_path in the session
        request.session['image_path'] = image_path
        
        new_image.save(image_path, format="PNG")

        message = 'Text has been encrypted in the image.'

    return render(request, 'encryption.html', {'message': message})

def download_image(request):
    # Ensure the file exists
     # Retrieve the image_path from the session
    image_path = request.session.get('image_path', '')
    if(image_path):
        response = FileResponse(open(image_path, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="encrypted_image.png"'
        return response
    else:
        return HttpResponseNotFound('Image not found')

def decryption_view(request):
    text = ''
    if request.method == 'POST':
        image_file = request.FILES['image']
        image = Image.open(image_file)

        # Convert to PNG if not already in that format
        if image.format != 'PNG':#checks whether the image format is not PNG.
            image = image.convert('RGBA')
            #image is converted to RGBA mode if it's not already
            #This ensures the image has the correct color channels.
            buffer = io.BytesIO()
            #A BytesIO object is created,
            # which is a binary stream (an in-memory bytes buffer).
            image.save(buffer, format="PNG")
            image = Image.open(buffer)

        # extract text from image
        text = extract_text_from_image(image)

    return render(request, 'decryption.html', {'text': text})


def extract_text_from_image(image):
    data = stepic.decode(image)
    # uses the decode function from the stepic library to extract the
    # hidden data from the given image. This hidden data is
    # typically stored as bytes.
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data
