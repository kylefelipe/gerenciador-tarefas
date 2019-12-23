from fastapi import FastAPI
from pydantic import BaseModel, constr
from uuid import UUID, uuid4
from enum import Enum
from starlette.responses import Response
from .modelo import Tarefa, TarefaEntrada
from .dados import Tarefas

app = FastAPI()


# class EstadosPossiveis(str, Enum):
#     finalizado = "finalizado"
#     nao_finalizado = "não finalizado"


# class TarefaEntrada(BaseModel):
#     titulo: constr(min_length=3, max_length=50)
#     descricao: constr(max_length=140)
#     estado: EstadosPossiveis = EstadosPossiveis.nao_finalizado


# class Tarefa(TarefaEntrada):
#     id: UUID


TAREFAS = Tarefas()


@app.get('/')
def home():
    home = {"titulo": "Olá mundo",
            "descição": "Pagina inicial"
            }
    return home


@app.get('/tarefas')
def listar():
    return TAREFAS.listar()


@app.get("/tarefas/{id_item}", response_model=Tarefa)
def buscar_item(id_item: UUID, response: Response):
    busca = TAREFAS.pegar_item(id_item)
    if not busca:
        response.status_code = 404
        return None
    return TAREFAS.pegar_item(id_item)


@app.post('/tarefas', response_model=Tarefa, status_code=201)
def criar(tarefa: TarefaEntrada):
    """Criar DocString"""
    TAREFAS.criar(tarefa)
    return tarefa


@app.delete("/tarefas/{id_tarefa}", status_code=204)
def deletar(id_tarefa: UUID, response: Response):
    remover = TAREFAS.deletar(id_tarefa)
    if not remover:
        response.stauts_code = 404
        return None
    return TAREFAS
