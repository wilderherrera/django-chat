from chat.service.chat.chat_service import ChatService
from chat.repository.chat.chat_repository_redis_impl import ChatRepositoryRedisImpl
from chat.repository.chat_room.chat_room_repository_impl import ChatRoomRepositoryImpl
from chat.models import ChatRoom
from chat.service.chat_room.chat_room_service import ChatRoomService
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    rooms = ChatRoomService(ChatRoomRepositoryImpl(ChatRoom)).get_rooms()
    context = {"user": request.user, "rooms": rooms}
    return render(request, "home.html", context)


def create_room(request):
    new_room_name = ChatRoomService(ChatRoomRepositoryImpl(ChatRoom)).get_new_room_name()
    print(new_room_name)
    return redirect("chat_room", room_name=new_room_name)


def room(request, room_name):
    chat_service = ChatService(ChatRepositoryRedisImpl())
    context = {"messages": chat_service.get_all(request, room_name),
               'username': request.user.username,
               'email   ': request.user.email,
               "room_name": room_name}
    return render(request, "room.html", context)


def get_all(request):
    pass
