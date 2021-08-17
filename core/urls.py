from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("bookr/", include("bookr.urls")),
    path('admin/', admin.site.urls),
    path("review/", include("review.urls")),
]
