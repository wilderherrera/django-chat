import logging

from channels.generic.websocket import AsyncWebsocketConsumer
import json
import time
from chat.repository.chat.chat_repository_redis_impl import ChatRepositoryRedisImpl
from chat.service.chat.chat_service import ChatService
from chat.service.chat_room.chat_room_service import ChatRoomService
from chat.models import ChatRoom
from chat.repository.chat_room.chat_room_repository_impl import ChatRoomRepositoryImpl
from datetime import datetime


class ChatConsumer(AsyncWebsocketConsumer):
    logger = logging.getLogger(__name__)

    async def connect(self):
        self.roomGroupName = self.scope["url_route"]["kwargs"]["room_name"]
        user = self.scope['user']
        if user.is_authenticated == False:
            await self.send({"close": True})
            logging.warning("User no authorized attempt to use the socket")
        else:
            print(self.channel_name)
            try:
                await self.channel_layer.group_add(
                    self.roomGroupName,
                    self.channel_name
                )
            except Exception as error:
                self.logger.critical("Error creating channel layer..." + str(error))
                await self.send({"close": True})
                return
            chat_room_service = ChatRoomService(ChatRoomRepositoryImpl(ChatRoom))
            chat_room_created = await chat_room_service.create_chat_room(self.roomGroupName)
            await chat_room_service.add_user_to_chat_room(chat_room_created, user)
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        logging.warning("Here")
        text_data_json = json.loads(text_data)
        user = self.scope['user']
        text_data_json["username"] = user.username
        text_data_json["email"] = user.email
        message = text_data_json["message"]
        await ChatService(ChatRepositoryRedisImpl()).create_message(text_data_json, user.id, self.roomGroupName)
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "user_id": user.id,
                "email": user.email,
                "username": user.username,
                "created_at": text_data_json["created_at"]
            })

    async def sendMessage(self, event):
        await self.send(text_data=json.dumps(event))
