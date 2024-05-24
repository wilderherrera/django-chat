import datetime

from channels.testing import WebsocketCommunicator, ChannelsLiveServerTestCase
from chat.channels.chat_consumer import ChatConsumer
from django.test import TestCase, override_settings
from django.urls import path
from channels.routing import URLRouter
from django.contrib.auth.models import User
import json
from chatRealTime import settings


class MyTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user_test", password="12456789", email="user_test@tests.com")

    async def test_my_consumer_without_limit(self):
        application = URLRouter([
            path("ws/chat/<str:room_name>", ChatConsumer.as_asgi()),
        ])
        communicator = WebsocketCommunicator(application, "ws/chat/chat_1")
        communicator.scope["user"] = self.user
        connected, subprotocol = await communicator.connect()
        assert connected
        # Test sending text
        data = {"type": "sendMessage",
                "message": 'Hello',
                "user_id": self.user.id,
                "email": self.user.email,
                "username": self.user.username,
                "created_at": str(datetime.datetime.now())}

        json_data = json.dumps(data)
        await communicator.send_to(text_data=json_data)
        response = await communicator.receive_from()
        for _ in range(10):
            assert self.user.email in response
            await communicator.send_to(text_data=json_data)
        # Close
        await communicator.disconnect()
