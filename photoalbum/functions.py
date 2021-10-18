def handle_uploaded_file(f):
    with open('photoalbum/image/', 'r') as destination:
        for chunk in f.chunks():
            destination.write(chunk)