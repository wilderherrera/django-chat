from chat.models import Chat
from chat.repository.chat import chat_repository_i
from channels.db import database_sync_to_async


class ChatRepositoryImpl(chat_repository_i.ChatRepositoryI):
    chat_model: Chat

    def __init__(self, chat_model: Chat.__class__):
        self.chat_model = chat_model()

    def get_all(self, request) -> [Chat]:
        return self.chat_model.pagination(request)

    @database_sync_to_async
    def create_message(self, message: dict):
        print("Save")
        chat = Chat()
        chat.content = message["message"]
        chat.user_id = 1
        chat.save()
