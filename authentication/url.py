from django.urls import path, include
from authentication.views.create_user_view import UserCreator

urlpatterns = [
    path("v1/sign_up", UserCreator.as_view(), name="create_user"),
    path("v1/", include("django.contrib.auth.urls")),
]
