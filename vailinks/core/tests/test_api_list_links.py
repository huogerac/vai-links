import pytest
from unittest.mock import ANY

from vailinks.core.models import Link


def test_nao_deve_permitir_listar_link_sem_login(client):
    # Dado um usuário anônimo

    # Quando tentamos listar itens
    resp = client.get("/api/core/links/list")

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 401


@pytest.mark.django_db
def test_deve_retornar_lista_vazia(client, logged_jon):
    # Quando tentamos listar itens
    resp = client.get("/api/core/links/list")
    data = resp.json()

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 200
    assert data.get("links") == []


@pytest.mark.django_db
def test_deve_listar_link_com_login(client, logged_jon):
    # Dado um item criado
    Link.objects.create(description="walk the dog")

    # Quando listamos
    resp = client.get("/api/core/links/list")
    data = resp.json()

    # Entao
    assert resp.status_code == 200
    assert data == {
        "links": [{"description": "walk the dog", "keyword": "", "link": "", "id": ANY}]
    }
