from django.urls import path

from . import views

app_name = "restaurant"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("map/", views.MapView.as_view(), name="map"),
    path("about/", views.AboutView.as_view(), name="about")
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("suggestions/", views.suggest, name="suggestion"),
    # path("suggestions/post", views.post, name="post"),
    # path("suggestions/list", views.List.as_view(), name="list"),
]
