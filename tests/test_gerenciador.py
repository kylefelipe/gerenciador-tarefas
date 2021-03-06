from starlette.testclient import TestClient
from gerenciador_tarefas.gerenciador import app, TAREFAS

# Testando o GET


def test_quando_listar_tarefas_devo_ter_como_retorno_de_status200():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200


def test_quando_listar_tarefas_formato_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.headers["Content-Type"] == "application/json"


def test_quando_listar_tarefas_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)


def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_id():
    TAREFAS.append({"id": 1})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "id" in resposta.json().pop()
    TAREFAS.clear()


def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_titulo():
    TAREFAS.append({"titulo": 'titulo 1'})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "titulo" in resposta.json().pop()
    TAREFAS.clear()


def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_descricao():
    TAREFAS.append({"descricao": "descricao 1"})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "descricao" in resposta.json().pop()
    TAREFAS.clear()


def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_um_estado():
    TAREFAS.append({"estado": "finalizado"})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "estado" in resposta.json().pop()
    TAREFAS.clear()

# Testando o POST


def test_recurso_tarefas_deve_aceitar_o_verbo_post():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas")
    assert resposta.status_code != 405
    TAREFAS.clear()


def test_quando_uma_tarefa_e_submetida_deve_possuir_um_titulo():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 422
    TAREFAS.clear()


def test_titulo_da_tarefa_deve_possuir_minimo_3_carateres():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={"titulo": 2 * "*"})
    assert resposta.status_code == 422
    TAREFAS.clear()


def test_titulo_da_tarefa_deve_possuir_maximo_50_caracteres():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={"titulo": 51 * "*"})
    assert resposta.status_code == 422
    TAREFAS.clear()


def test_descricao_da_tarefa_pode_conter_no_maximo_140_caracteres():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={"titulo": "titulo", "descicao": "*" * 141})
    assert resposta.status_code == 422
    TAREFAS.clear()


def test_quando_criar_uma_tarefa_a_mesma_deve_ser_retornada():
    cliente = TestClient(app)
    tarefa = {"titulo": "titulo", "descricao": "descricao"}
    resposta = cliente.post("/tarefas", json=tarefa)
    copia_resposta = resposta.json()
    excluir = ['id', 'estado']
    for exc in excluir:
        copia_resposta.pop(exc)
    print(copia_resposta)
    assert copia_resposta == tarefa
    TAREFAS.clear()


def test_quando_criar_uma_tarefa_seu_id_deve_ser_unico():
    cliente = TestClient(app)
    tarefa1 = {"titulo": "titulo1", "descricao": "descricao1"}
    tarefa2 = {"titulo": "titulo2", "descricao": "descricao2"}
    resposta1 = cliente.post("/tarefas", json=tarefa1)
    resposta2 = cliente.post("/tarefas", json=tarefa2)
    assert resposta1.json()["id"] != resposta2.json()["id"]
    TAREFAS.clear()


def test_quando_criar_uma_tarefa_seu_estado_padrao_e_nao_finalizado():
    cliente = TestClient(app)
    tarefa = {"titulo": "titulo", "descricao": "descricao"}
    resposta = cliente.post("/tarefas", json=tarefa)
    assert resposta.json()["estado"] == "não finalizado"
    TAREFAS.clear()

def test_quando_criar_uma_tarefa_codigo_de_status_retornado_deve_ser_201():
    cliente = TestClient(app)
    tarefa = {"titulo": "titulo", "descricao": "descricao"}
    resposta = cliente.post("/tarefas", json=tarefa)
    assert resposta.status_code == 201
    TAREFAS.clear()


def test_quando_criar_uma_nova_tarefa_esta_deve_persistida():
    cliente = TestClient(app)
    tarefa = {"titulo": "titulo", "descricao": "descricao"}
    resposta = cliente.post("/tarefas", json=tarefa)
    assert resposta.status_code == 201
    assert len(TAREFAS) == 1
    TAREFAS.clear()


def test_quando_deletar_uma_tarefa_existente_deve_retornar_204():
    client = TestClient(app)
    tarefa = {"titulo": "titulo1", "descricao": "descricao1"}
    cria = client.post("/tarefas", json=tarefa)
    id = cria.json()['id']
    resposta = client.delete(f"/tarefas/{id}")
    assert resposta.status_code == 204
    TAREFAS.clear()


def test_buscando_uma_tarefa_unica():
    client = TestClient(app)
    id = ''
    tarefas_teste = [{"titulo": "titulo1", "descricao": "descricao1"},
                     {"titulo": "titulo2", "descricao": "descricao2"}]
    for tarefa_cria in tarefas_teste:
        tarefa = client.post("/tarefas", json=tarefa_cria)
        id = tarefa.json()['id']
    assert len(id) == 1


def test_quando_deletar_uma_tarefa_inexistente_deve_retornar_404():
    client = TestClient(app)
    # tarefas_teste = [{"titulo": "titulo1", "descricao": "descricao1"},
    #                  {"titulo": "titulo2", "descricao": "descricao2"}]
    # for tarefa_cria in tarefas_teste:
    #     client.post("/tarefas", json=tarefa_cria)
    resposta = client.delete("/tarefas/a54a631a658dsa98asdf987sdf")
    assert resposta.status_code == 404
    TAREFAS.clear()
