from operator import itemgetter, attrgetter


tarefas = [{'titulo': 'tarefa 1', 'descricao': 'essa e a tarefa 1', 'id': 1, 'status': 'finalizada'},
           {'titulo': 'tarefa 2', 'descricao': 'essa e a tarefa 2', 'id': 2, 'status': 'não finalizada'},
           {'titulo': 'tarefa 3', 'descricao': 'essa e a tarefa 3', 'id': 3, 'status': 'finalizada'},
           {'titulo': 'tarefa 4', 'descricao': 'essa e a tarefa 4', 'id': 4, 'status': 'finalizada'}]

item = itemgetter('status')

sorted(tarefas, key=itemgetter('status'), reverse=True)

item = itemgetter('titulo')
filtro = list(filter(lambda tarefa: tarefa['titulo'] == 'tarefa 1', tarefas))
for i in filtro:
    print(tarefas.index(i))


def retorna_id(lista: list, filtro: list):
    ids = [lista.index(dado) for dado in filtro]
    return ids


lista_ids = retorna_id(tarefas, filtro)


def remove_item(lista_ids: list):
    for dado in lista_ids:
        print(dado)
        tarefas.pop(dado)
    return tarefas


remove_item(retorna_id(tarefas, filtro))