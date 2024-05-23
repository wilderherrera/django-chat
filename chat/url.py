from django.urls import path, re_path, include
from chat import views, chat_consumer
from authentication import url
import django.contrib.auth.urls

urlpatterns = [
    path("v1/home", views.index),
    path("chat/<str:room_name>/", views.room, name="room"),

]
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", chat_consumer.ChatConsumer.as_asgi()),
]
