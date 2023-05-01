from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts", views.index, name="index"),
    path("posts/<slug:post>", views.view, name="view"),
]
