from django.urls import path, re_path, include
from chat import views, chat_consumer
from authentication import url
import django.contrib.auth.urls
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("v1/home", login_required(views.index), name="home"),
    path("chat/<str:room_name>/", login_required(views.room), name="chat_room"),

]
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", chat_consumer.ChatConsumer.as_asgi()),
]
