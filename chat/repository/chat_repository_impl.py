import chat.models
from chat.repository import chat_repository_i
from django.core.paginator import Paginator


class ChatRepositoryImpl(chat_repository_i.ChatRepositoryI):
    def __init__(self, chat_model):
        self.chat_model = chat_model()

    def get_all(self, request) -> [chat.models.Chat]:
        return self.chat_model.pagination(request)
