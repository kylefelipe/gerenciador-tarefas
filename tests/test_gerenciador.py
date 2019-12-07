from starlette.testclient import TestClient
from gerenciador_tarefas.gerenciador import app, TAREFAS

# Testando o GET

def test_quando_listar_tarefas_devo_ter_como_retorno_de_status200():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200

def test_quando_listar_tarefas_formato_deve_ser_json():
    cliente = TestClient(app)
    resposta =  cliente.get("/tarefas")
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

def test_quando_uma_tarefa_e_submetida_deve_possuir_um_titulo():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 422

def test_titulo_da_tarefa_deve_possuir_entre_3_e_50_caracteres():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={"titulo": 2 * "*"})
    assert resposta.status_code == 422
    resposta = cliente.post("/tarefas", json={"titulo": 51 * "*"})
    assert resposta.status_code == 422

def test_descricao_da_tarefa_pode_conter_no_maximo_140_caracteres():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={"titulo": "titulo", "descicao": "*" * 141})
    assert resposta.status_code == 422