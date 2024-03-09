import logging

from vailinks.base.exceptions import BusinessError
from ..models import Link, Workspace

logger = logging.getLogger(__name__)


def add_link(new_link: str) -> dict:
    logger.info("SERVICE add new link")
    if not isinstance(new_link, str):
        raise BusinessError("Invalid description")

    if not new_link or not new_link.strip():
        raise BusinessError("Invalid description")

    link = Link(description=new_link)
    link.save()
    logger.info("SERVICE link created.")
    return link.to_dict_json()


def list_links():
    logger.info("SERVICE list links")
    links_list = Link.objects.all()
    return [item.to_dict_json() for item in links_list]


def search(workspace_name, query):
    logger.info("SERVICE find links")
    workspace = Workspace.objects.filter(name=workspace_name).first()
    if not workspace:
        raise BusinessError("Workspace not found")

    return Link.objects.filter(
        workspace_id=workspace.id, keyword__icontains=query
    ).first()
