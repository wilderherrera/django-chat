from chat.repository.chat_room import chat_room_repository_i
from chat.models import ChatRoom
from channels.db import database_sync_to_async
from django.contrib.auth.models import User


class ChatRoomRepositoryImpl(chat_room_repository_i.ChatRoomRepositoryI):
    def __init__(self, chat_room_model: ChatRoom.__class__):
        self.chat_room_model = chat_room_model

    @database_sync_to_async
    def create(self, name) -> ChatRoom:
        chat_room = self.chat_room_model.objects.filter(name=name)
        if chat_room:
            return chat_room[0]
        new_chat_room = ChatRoom()
        new_chat_room.name = name
        new_chat_room.save()
        return new_chat_room

    @database_sync_to_async
    def add_user(self, chat_room: ChatRoom, user: User) -> bool:
        if chat_room.users.filter(id=user.id).count() != 0:
            return False
        chat_room.users.add(user)
        return True

    def get_rooms(self):
        return self.chat_room_model.objects.all()
