from django.http import JsonResponse
from chat.service.chat.chat_service import ChatService
from chat.repository.chat.chat_repository_impl import ChatRepositoryImpl
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
    return render(request, "room.html", {"room_name": room_name})


def get_all(request):
    chat_service = ChatService(ChatRepositoryImpl(Chat))
    return JsonResponse(chat_service.get_all(request), safe=False)
