from django.db import models

from chat.utils.paginator_filter import PaginatorFilter
from django.contrib.auth.models import User


class ChatRoom(models.Model, PaginatorFilter):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(255, unique=True)
    users = models.ManyToManyField(User)

    class Meta:
        db_table = "chat_rooms"


class Chat(models.Model, PaginatorFilter):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chats"
