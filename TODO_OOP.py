import TODO_Test
from TODO_Test import *

def test_create_TodoItem():
    taskDescription = "Mow Lawn"
    item = TODO_Test(taskDescription)
    assert(item.description == taskDescription)