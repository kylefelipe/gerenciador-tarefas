from typing import List, Dict, Union
from uuid import UUID, uuid4
from .modelo import TarefaEntrada
from .opcoes_status import EstadosPossiveis

Item = Dict[str, Union[UUID, str, EstadosPossiveis]]


class Tarefas:

    TAREFAS: List[Item] = []

    def listar(self):
        return self.TAREFAS

    def criar(self, tarefa: Item) -> Item:
        nova_tarefa = tarefa.dict()
        nova_tarefa.update({"id": uuid4()})
        self.TAREFAS.append(nova_tarefa)
        return nova_tarefa

    def deletar(self, id_tarefa: UUID):
        filtro = list(filter(lambda tarefa: tarefa['id'] == id_tarefa,
                             self.TAREFAS))
        ids = [self.TAREFAS.index(dado) for dado in filtro]

        if ids:
            for dado in ids:
                self.TAREFAS.pop(dado)
            return self.TAREFAS
        return None

    def pegar_item(self, id_tarefa: UUID) -> Item:
        item = filter(lambda tarefa: tarefa["id"] == id_tarefa,
                      self.TAREFAS)
        if not item:
            return None
        return list(item)[0]
