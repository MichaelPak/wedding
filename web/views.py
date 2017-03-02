from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dress_code(request):
    return render(request, 'single.html')


def location(request):
    return render(request, 'single.html')
