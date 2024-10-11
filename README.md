# Stegano-project-CGV

This project implements Image Steganography, a technique for hiding secret messages within an image file. Using this tool, a user can encode their message into an image such that the message is invisible to the naked eye but can be decoded by the intended recipient with the appropriate algorithm. The primary goal of this project is to provide a simple yet effective way to communicate securely by concealing the message within the image without altering its visible quality.

Key Features:
Message Encoding: Embeds a hidden message into an image file.
Message Decoding: Extracts the hidden message from the image.
Lossless Embedding: The quality of the image remains intact even after encoding the message.
User-friendly Interface: Provides an intuitive way for users to input images and messages for encoding and decoding.

How It Works:
Encoding: The user provides an image and a text message. The algorithm embeds the message into the image's pixel data in such a way that it is imperceptible.
Decoding: The recipient runs the decoding algorithm on the image to retrieve the hidden message.
