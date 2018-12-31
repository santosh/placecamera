from django.http import HttpResponse
from django.shortcuts import render
from .imagemaker import ImageMaker


def home(request):
    return render(request, 'index.html')


def placecameraview(request):
    path = request.path.lstrip('/')

    image = ImageMaker(path).make_image()

    response = HttpResponse(content_type="image/jpeg")

    image.save(response, "JPEG")

    return response
