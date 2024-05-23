import chat.models


class ChatRepositoryI:
    def get_all(self, request) -> [chat.models.Chat]:
        pass

    def create_message(self, message: dict):
        pass
