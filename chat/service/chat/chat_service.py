import chat.models
from chat.repository.chat.chat_repository_i import ChatRepositoryI


class ChatService:
    def __init__(self, chat_repo: ChatRepositoryI):
        self.chat_repo = chat_repo

    def get_all(self, request, chat_room) -> [chat.models.Chat]:
        return self.chat_repo.get_all(request, chat_room)

    async def create_message(self, message: dict, user_id: int, chat_room: str):
        await self.chat_repo.create_message(message, user_id, chat_room)
