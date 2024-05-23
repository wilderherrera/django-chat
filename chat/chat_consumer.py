from channels.generic.websocket import AsyncWebsocketConsumer
import json
import chat.models
from chat.repository.chat.chat_repository_impl import ChatRepositoryImpl
from chat.service.chat.chat_service import ChatService
from chat.service.chat_room.chat_room_service import ChatRoomService
from chat.models import ChatRoom
from chat.repository.chat_room.chat_room_repository_impl import ChatRoomRepositoryImpl


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = self.scope["url_route"]["kwargs"]["room_name"]
        user = self.scope['user']
        if user.is_authenticated == False:
            await self.send({"close": True})
        else:
            await self.channel_layer.group_add(
                self.roomGroupName,
                self.channel_name
            )
            chat_room_service = ChatRoomService(ChatRoomRepositoryImpl(ChatRoom))
            chat_room_created = await chat_room_service.create_chat_room(self.roomGroupName)
            await chat_room_service.add_user_to_chat_room(chat_room_created, user)
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        chat_service = ChatService(ChatRepositoryImpl(chat.models.Chat))
        await chat_service.create_message(text_data_json)
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": "Wilder",
            })

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"message": message, "username": username}))
