from django.db import models

from chat.utils.paginator_filter import PaginatorFilter


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(255)
    last_name = models.CharField(255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"


class Chat(models.Model, PaginatorFilter):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chats"
