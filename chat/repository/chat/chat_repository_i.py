import chat.models


class ChatRepositoryI:
    def get_all(self, request, chat_room) -> [chat.models.Chat]:
        pass

    def create_message(self, message: dict, user_id: int, chat_room: str):
        pass
