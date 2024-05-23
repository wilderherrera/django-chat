from chat.models import ChatRoom


class ChatRoomRepositoryI:
    def create(self, name) -> ChatRoom:
        pass

    def add_user(self, chat_room: ChatRoom, user_id) -> bool:
        pass

    def get_rooms(self):
        pass
