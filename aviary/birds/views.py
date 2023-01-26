from django.shortcuts import render, get_object_or_404
from .models import Bird

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def birds(request):
    data = {"birds": Bird.objects.all()}
    return render(request, "birds.html", data)

def bird(request, id):
    bird = get_object_or_404(Bird, pk=id)
    data = {"bird": bird}
    return render(request, "bird.html", data)
