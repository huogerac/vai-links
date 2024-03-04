import pytest

from vailinks.core.models import Link
from vailinks.core.service import links_svc
from vailinks.base.exceptions import BusinessError


@pytest.mark.django_db
def test_deve_inserir_uma_nova_tarefa():
    new_item = links_svc.add_link("ABC")

    item = Link.objects.all().first()

    assert item.id == new_item.get("id")
    assert item.description == new_item.get("description")


@pytest.mark.django_db
def test_deve_retornar_um_erro_ao_cadastrar_item_sem_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = links_svc.add_link(None)

    # Então
    assert str(error.value) == "Invalid description"


@pytest.mark.django_db
def test_deve_retornar_um_erro_ao_cadastrar_item_com_espacos_na_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = links_svc.add_link("    ")

    # Então
    assert str(error.value) == "Invalid description"


@pytest.mark.django_db
def test_deve_aceitar_apenas_tipo_string_na_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = links_svc.add_link(1000)

    # Então
    assert str(error.value) == "Invalid description"
