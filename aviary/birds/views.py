from django.shortcuts import render, get_object_or_404, redirect
from .models import Bird

from .forms import NewBirdForm

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

def create(request):
    if request.method == "POST":
        bird = NewBirdForm(request.POST)
        if bird.is_valid():
            id = bird.save().id
            return redirect("birds-bird", id=id)
    else:
        form = NewBirdForm()
    data = {"form": form}
    return render(request, "new.html", data)