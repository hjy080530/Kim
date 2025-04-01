from typing import List
from datetime import datetime

from fastAPI.applicationProgrammingDevelopment.ch05.error import Missing, Duplicate
from fastAPI.applicationProgrammingDevelopment.ch05.model.todo import TodoResponse, Todo

_todos = [
    TodoResponse(
        todo_id=0,
        task="study fastapi",
        completed=0,
        created_at="2025-03-01"
    ),
    TodoResponse(
        todo_id=1,
        task="study_db",
        completed=1,
        created_at="2025-03-01"
    )
]

todo_id = 1

def get_all() -> List[TodoResponse]:
    return _todos

def get_one(todo: Todo) -> TodoResponse:
    _todo = next((x for x in _todos if x.task == todo.task), None)
    if _todo is None:
        raise Missing(msg=f"{todo.task}가 없음")
    return _todo

def create(todo: Todo) -> TodoResponse:
    global todo_id
    todo_id += 1
    try:
        get_one(todo)
        raise Duplicate(msg=f"{todo.task}가 이미 있습니다.")
    except Missing:
        pass  # 예외 발생 시 새로 추가

    new_todo = TodoResponse(
        todo_id=todo_id,
        task=todo.task,
        completed=0,
        created_at=datetime.now()
    )
    _todos.append(new_todo)
    return _todos[-1]  # 마지막 추가된 todo 반환

def delete(todo: Todo) -> bool:
    _todo = get_one(todo)
    _todos.remove(_todo)
    return True

def modify(todo: Todo) -> TodoResponse:
    temp = get_one(todo)
    temp.completed = not temp.completed
    return temp