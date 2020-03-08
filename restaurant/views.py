from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import FoodPlace

# Create your views here.
def redirect_view(request):
    response = redirect("restaurant/")
    return response


class IndexView(generic.ListView):
    template_name = "restaurant/index.html"
    model = FoodPlace


class MapView(generic.ListView):
    template_name = "restaurant/map.html"
    model = FoodPlace


class AboutView(generic.ListView):
    template_name = "restaurant/map.html"
    model = FoodPlace


def get_current_location(request):
    lat = POST.get("lat")
    lon = POST.get("long")

