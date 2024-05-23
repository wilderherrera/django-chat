from chat.repository.chat_room.chat_room_repository_i import ChatRoomRepositoryI
from chat.models import ChatRoom


class ChatRoomService:
    def __init__(self, chat_room_repo: ChatRoomRepositoryI):
        self.chat_room_repo = chat_room_repo

    def get_new_room_name(self):
        return "chat_" + str(self.chat_room_repo.count_all())

    def get_rooms(self):
        return self.chat_room_repo.get_rooms()

    async def create_chat_room(self, name) -> ChatRoom:
        return await self.chat_room_repo.create(name)

    async def add_user_to_chat_room(self, chat_room: ChatRoom, user_id: int):
        await self.chat_room_repo.add_user(chat_room, user_id)
