import chat.models


class ChatRepositoryI:
    def get_all(self, request) -> [chat.models.Chat]:
        pass
