import pytest

from vailinks.core.models import Link
from vailinks.core.service import links_svc


@pytest.mark.django_db
def test_deve_retornar_lista_vazia():
    itens_list = links_svc.list_links()
    assert itens_list == []


@pytest.mark.django_db
def test_deve_listar_com_10_iten():
    # Dado 10 itens criados
    itens = [
        Link(
            description=f"Links nro ${number}",
            keyword=f"{number}",
            link=f"http://link${number}.com",
        )
        for number in range(1, 11)
    ]
    Link.objects.bulk_create(itens)

    itens_list = links_svc.list_links()

    assert len(itens_list) == 10
