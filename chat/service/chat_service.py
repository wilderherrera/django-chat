import chat.models
from chat.repository.chat_repository_i import ChatRepositoryI


class ChatService:
    def __init__(self, chat_repo: ChatRepositoryI):
        self.chat_repo = chat_repo

    def get_all(self, request) -> [chat.models.Chat]:
        return self.chat_repo.get_all(request)
