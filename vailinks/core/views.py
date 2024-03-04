# coding: utf-8
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from ninja import Router

from .schemas import ListLinksSchema, LinkSchema, LinkSchemaIn
from .service import links_svc

logger = logging.getLogger(__name__)
router = Router()


@router.post("/links/add", response={201: LinkSchema})
@csrf_exempt
def add_link(request, link: LinkSchemaIn):
    logger.info("API add new link.")
    new_link = links_svc.add_link(link.description)

    return JsonResponse(new_link, status=201)


@router.get("/links/list", response=ListLinksSchema)
def list_links(request):
    logger.info("API list links")
    links = links_svc.list_links()
    return JsonResponse({"links": links})


@router.get("/search")
def search_link(request, q: str):
    link = links_svc.find(q)
    if not link:
        return JsonResponse(
            {"message": "Opps! Não temos link para esta palavra", "keyword": q}
        )

    return redirect(link.link)
