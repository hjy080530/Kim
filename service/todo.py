#비지니스 함수들
from typing import List

from fastAPI.applicationProgrammingDevelopment.ch05.error import Missing
from fastAPI.applicationProgrammingDevelopment.ch05.model.todo import TodoResponse, Todo
from fastAPI.applicationProgrammingDevelopment.ch05.fake import todo as data


# from ch05.model.todo import TodoResponse, Todo
# from ch05.fake import todo as data


def get_all() -> List[TodoResponse]:
    return data.get_all()


def get_one(todo: Todo) -> TodoResponse:
    _todo = next((x for x in todos_ if x.task == todo.task), None)
    if _todo is None:
        raise Missing(msg=f"{todo.task} not found")
    return _todo  # `_todo` 객체를 반환

def create(todo:Todo) -> TodoResponse:
    return data.create(todo)

def delete(todo:Todo) -> bool:
    return data.delete(todo)

def modify(todo:Todo) -> TodoResponse:
    return data.modify(todo)