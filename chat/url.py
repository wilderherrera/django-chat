from django.urls import path
from chat import views

urlpatterns = [
    path("v1/chats", views.get_all)
]
