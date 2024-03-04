import pytest
import mock
from unittest.mock import ANY

from vailinks.core.models import Link
from vailinks.base.exceptions import BusinessError


def test_nao_deve_permitir_criar_link_sem_login(client):
    # Dado um usuário anônimo

    # Quando tentamos adicionar um item
    resp = client.post("/api/core/links/add", {"new_link": "walk the dog"})

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 401


@pytest.mark.django_db
def test_deve_criar_link_com_login(client, logged_jon):
    # Dado um usuario logado
    payload = {"description": "estudar pytest"}

    # Quando adicionamos um item
    resp = client.post("/api/core/links/add", payload, content_type="application/json")

    # Entao
    assert resp.status_code == 201
    assert resp.json() == {
        "id": ANY,
        "description": "estudar pytest",
        "keyword": "",
        "link": "",
    }


@pytest.mark.django_db
def test_deve_falhar_com_input_invalido(client, logged_jon):
    # Dado uma entrada inválida
    payload = {}

    # Quando tentamos adicionar
    resp = client.post("/api/core/links/add", payload, content_type="application/json")
    msg = resp.json()

    # Então
    assert resp.status_code == 422  # BAD REQUEST
    assert msg == {
        "message": "[INVALID INPUT] body.link.description: field required (value_error.missing)",
    }


@pytest.mark.django_db
def test_deve_falhar_com_input_menor_que_minimo_necessario(client, logged_jon):
    # Dado uma entrada inválida
    payload = {"description": "??"}

    # Quando tentamos adicionar
    resp = client.post("/api/core/links/add", payload, content_type="application/json")
    msg = resp.json()

    # Então
    assert resp.status_code == 422  # BAD REQUEST
    assert resp.json() == {
        "message": "[INVALID INPUT] body.link.description: It must be at least 3 characteres long. (value_error)",
    }


@pytest.mark.django_db
def test_deve_deve_converter_descricao_para_string(client, logged_jon):
    # Dado uma entrada inválida
    payload = {"description": 4242}

    # Quando tentamos adicionar
    resp = client.post("/api/core/links/add", payload, content_type="application/json")
    msg = resp.json()

    # Então
    assert resp.status_code == 201
    assert resp.json() == {
        "id": ANY,
        "description": "4242",
        "keyword": "",
        "link": "",
    }


@pytest.mark.django_db
def test_deve_falhar_quando_description_contem_algo_diferente_de_string(
    client, logged_jon
):
    # Dado uma entrada inválida
    payload = {"description": {"objeto": "invalido"}}

    # Quando tentamos adicionar
    resp = client.post("/api/core/links/add", payload, content_type="application/json")
    msg = resp.json()

    # Então
    assert resp.status_code == 422
    assert resp.json() == {
        "message": "[INVALID INPUT] body.link.description: str type expected (type_error.str)",
    }


@pytest.mark.django_db
def test_deve_receber_erro_enviado_pela_classe_de_servico(client, logged_jon):
    # Dado uma entrada inválida
    payload = {"description": "INVALID DESCRIPTION"}

    # Quando tentamos adicionar
    with mock.patch("vailinks.core.service.links_svc.add_link") as add_link_mock:
        add_link_mock.side_effect = BusinessError("Invalid description")
        resp = client.post(
            "/api/core/links/add", payload, content_type="application/json"
        )
        msg = resp.json()

    # Então
    assert resp.status_code == 400
    assert msg == {"message": "[ERROR] Invalid description"}
