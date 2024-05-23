from chat.models import Chat
from chat.repository.chat import chat_repository_i
from channels.db import database_sync_to_async
from django.core.cache import cache
import logging


class ChatRepositoryRedisImpl(chat_repository_i.ChatRepositoryI):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.cache = cache

    def get_all(self, request, chat_room) -> [dict]:
        return cache.get(self.get_key(chat_room), [])

    @database_sync_to_async
    def create_message(self, message: dict, user_id: int, chat_room: str):
        try:
            cache_key = self.get_key(chat_room)
            message_cache = self.cache.get(cache_key, [])
            message_cache.append(message)
            self.cache.set(cache_key, message_cache, self.get_timeout())
        except Exception as error:
            self.logger.critical("Error creating message in cache ..." + str(error))

    def get_key(self, chat_room: str) -> str:
        return "_chat_room_" + chat_room

    def get_timeout(self) -> [int, None]:
        return None
