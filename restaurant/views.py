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

class MenuView(generic.ListView):
    template_name = "restaurant/menu.html"
    model = FoodPlace

class AvailableView(generic.ListView):
    template_name = "restaurant/have.html"
    model = FoodPlace


class DateView(generic.ListView):
    template_name = "restaurant/date.html"
    model = FoodPlace


class RandomView(generic.ListView):
    template_name = "restaurant/random.html"
    model = FoodPlace

