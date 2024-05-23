from django.http import JsonResponse
from chat.service.chat.chat_service import ChatService
from chat.repository.chat.chat_repository_redis_impl import ChatRepositoryRedisImpl
from chat.repository.chat_room.chat_room_repository_impl import ChatRoomRepositoryImpl
from chat.models import ChatRoom
from chat.service.chat_room.chat_room_service import ChatRoomService
from chat.models import Chat
from django.shortcuts import render


def index(request):
    rooms = ChatRoomService(ChatRoomRepositoryImpl(ChatRoom)).get_rooms()
    print(rooms)
    context = {"user": request.user, "rooms": rooms}

    return render(request, "home.html", context)


def room(request, room_name):
    chat_service = ChatService(ChatRepositoryRedisImpl())
    context = {"messages": chat_service.get_all(request, room_name),
               'username': request.user.username,
               'email   ': request.user.email,
               "room_name": room_name}
    return render(request, "room.html", context)


def get_all(request):
    pass
