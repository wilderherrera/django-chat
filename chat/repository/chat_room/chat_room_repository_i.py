from chat.models import ChatRoom
from channels.db import database_sync_to_async


class ChatRoomRepositoryI:
    @database_sync_to_async
    def create(self, name) -> ChatRoom:
        pass

    def add_user(self, chat_room: ChatRoom, user_id) -> bool:
        pass

    def get_rooms(self):
        pass

    def count_all(self) -> int:
        pass
