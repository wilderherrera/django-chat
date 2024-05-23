# Generated by Django 5.0.4 on 2024-05-21 02:09

import chat.utils.paginator_filter
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chat_table_alter_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name=255)),
                ('users', models.ManyToManyField(to='chat.user')),
            ],
            options={
                'db_table': 'chat_rooms',
            },
            bases=(models.Model, chat.utils.paginator_filter.PaginatorFilter),
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='chat.chatroom'),
            preserve_default=False,
        ),
    ]