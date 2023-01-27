from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="birds-home"),
    path("about/", views.about, name="birds-about"),
    path("birds/", views.birds, name="birds-birds"),
    path("birds/<int:id>/", views.bird, name="birds-bird"),
    path("birds/new/", views.create, name="birds-new")
]