from fastapi import FastAPI
from pydantic import BaseModel, constr
from uuid import UUID, uuid4

app = FastAPI()


class TarefaEntrada(BaseModel):
    titulo: constr(min_length=3, max_length=50)
    descricao: constr(max_length=140)


class Tarefa(TarefaEntrada):
    id: UUID


TAREFAS = []


@app.get('/tarefas')
def listar():
    return TAREFAS


@app.post('/tarefas', response_model=Tarefa)
def criar(tarefa: TarefaEntrada):
    """Criar DocString"""
    nova_tarefa = tarefa.dict()
    nova_tarefa.update({"id": uuid4()})
    return nova_tarefa
