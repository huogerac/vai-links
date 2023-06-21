# coding: utf-8

from django.http import JsonResponse


from ninja import Router

from .schemas import ListLinksSchema, LinkSchema, LinkSchemaIn


from .service import links_svc


router = Router()


@router.post("/links/add", response=LinkSchema)
def add_link(request, link: LinkSchemaIn):
    new_link = links_svc.add_link(link.description)

    return JsonResponse(new_link)


@router.get("/links/list", response=ListLinksSchema)
def list_links(request):
    links = links_svc.list_links()
    return JsonResponse({"links": links})
