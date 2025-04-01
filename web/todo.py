#엔드포인트
from typing import List

from fastapi import APIRouter

from fastAPI.applicationProgrammingDevelopment.ch05.error import Duplicate,Missing
from fastAPI.applicationProgrammingDevelopment.ch05.model.todo import TodoResponse,Todo
from fastAPI.applicationProgrammingDevelopment.ch05.service import todo as service

#from ch05.error import Duplicate
#from ch05.model.todo import TodoResponse, Todo
#from ch05.service import todo as service

router = APIRouter(prefix="/todo")

@router.get('')
def get_all() -> List[TodoResponse]:
    return service.get_all()

@router.get('/{task}')
def get_one(task:str) -> TodoResponse:
    #from ch05.error import Missing

    try :
        return service.get_one(Todo(task=task))
    except Missing as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=e.msg)

@router.post('/')
def create(todo: Todo) -> TodoResponse:
    try :
        return service.create(todo)
    except Duplicate as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=409, detail=e.msg)

@router.delete('/{task}')
def delete(task:str) -> bool:
    return service.delete(Todo(task=task))

@router.patch("/{task}")
def modify(task:str) -> TodoResponse:
    return service.modify(Todo(task=task))