from unittest.mock import ANY

from vailinks.accounts.models import User
from vailinks.accounts.tests import fixtures
from vailinks.core.models import Link


def test_criar_link_sem_login(client):
    resp = client.post("/api/core/links/add", {"new_link": "walk the dog"})
    assert resp.status_code == 401


def test_criar_link_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    payload = {"description": "estudar pytest"}
    resp = client.post("/api/core/links/add", payload, content_type="application/json")
    assert resp.status_code == 200


def test_listar_link_com_login(client, db):
    fixtures.user_jon()
    Link.objects.create(description="walk the dog")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/core/links/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {"links": [{"description": "walk the dog", "id": ANY}]}
