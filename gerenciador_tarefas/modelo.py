from uuid import UUID
from pydantic import BaseModel, constr
from .opcoes_status import EstadosPossiveis


class TarefaEntrada(BaseModel):
    titulo: constr(min_length=3, max_length=50)
    descricao: constr(max_length=140)
    estado: EstadosPossiveis = EstadosPossiveis.nao_finalizado


class Tarefa(TarefaEntrada):
    id = UUID