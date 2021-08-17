from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home-bookr"),
    path("search/", search, name="search-bookr")
]
