from django.urls import path

from . import views

app_name = "restaurant"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("map/", views.MapView.as_view(), name="map"),
    # path("about/", views.IndexView.as_view(), name="about"),
    path("date/", views.DateView.as_view(), name="date"),
    path("random/", views.RandomView.as_view(), name="random"),
    path("menu/", views.MenuView.as_view(), name="menu"),
    path("available/", views.AvailableView.as_view(), name="menu"),
]
