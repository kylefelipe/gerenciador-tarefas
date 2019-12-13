from operator import itemgetter, attrgetter


tarefas = [{'titulo': 'tarefa 1', 'descricao': 'essa e a tarefa 1', 'id': 1, 'status': 'finalizada'},
           {'titulo': 'tarefa 2', 'descricao': 'essa e a tarefa 2', 'id': 2, 'status': 'não finalizada'},
           {'titulo': 'tarefa 3', 'descricao': 'essa e a tarefa 3', 'id': 3, 'status': 'finalizada'},
           {'titulo': 'tarefa 4', 'descricao': 'essa e a tarefa 4', 'id': 4, 'status': 'finalizada'}]

item = itemgetter('status')

sorted(tarefas, key=itemgetter('status'), reverse=True)


