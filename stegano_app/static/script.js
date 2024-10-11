document.addEventListener('mousedown', function() {
    document.body.classList.add('custom-cursor');
});

document.addEventListener('mouseup', function() {
    document.body.classList.remove('custom-cursor');
});
