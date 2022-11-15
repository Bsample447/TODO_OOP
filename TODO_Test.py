from datetime import datetime

class TodoItem:
    def __init_(self, description):
        self.description = description
        self.complete = False
        self.creationDate = datetime.now()

def save(self):
    return f"False|{self.description}"

def markComplete(self):
    self.complete = True




def test_empty_todo():
    try:
        create_TodoItem("")
        