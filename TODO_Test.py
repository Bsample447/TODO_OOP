from datetime import datetime

class TodoItem:
    def __init_(self, description):
        self.description = description
        self.complete = False
        self.creationDate = datetime.now()