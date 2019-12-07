from fastapi import FastAPI
from pydantic import BaseModel, constr

app = FastAPI()

class Tarefa(BaseModel):
    titulo: constr(min_length=3, max_length=50)
    descricao: constr(max_length(140))

TAREFAS = []

@app.get('/tarefas')
def listar():
    return TAREFAS

@app.post('/tarefas')
def criar(tarefa: Tarefa):
    pass