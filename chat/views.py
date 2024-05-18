import json

from django.http import HttpResponse, JsonResponse
from chat.service.chat_service import ChatService
from chat.repository.chat_repository_impl import ChatRepositoryImpl
from chat.models import Chat
from django.core import serializers


def index(request):
    return JsonResponse({"Wilder": "Herrera"})


def get_all(request):
    chat_service = ChatService(ChatRepositoryImpl(Chat))
    return JsonResponse(chat_service.get_all(request), safe=False)
