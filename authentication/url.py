from django.urls import path, include

urlpatterns = [
    path("v1/", include("django.contrib.auth.urls")),
]
