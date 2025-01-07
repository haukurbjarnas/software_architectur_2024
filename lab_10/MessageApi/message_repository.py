class MessageRepository:
    def __init__(self):
        self.base = {}
        self.ids = 1

    def save_message(self, message) -> int:
        # TODO: save message to persistent storage and return id
        self.ids += 1
        self.base[id] = message

    def get_message(self, id: int) -> str:
        # TODO: return message with id from storage
        try:
            return self.base[id]
        except KeyError:
            pass
