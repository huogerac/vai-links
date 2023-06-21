# coding: utf-8

from django.http import JsonResponse
from django.shortcuts import redirect
from ninja import Router

from ..core.service import links_svc

router = Router()


@router.get("/")
def search_link(request, q: str):
    link = links_svc.find(q)
    if not link:
        return JsonResponse(
            {"message": "Opps! Não temos link para esta palavra", "keyword": q}
        )

    return redirect(link.link)
