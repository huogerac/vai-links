import os
from django.db import connection
from django.http import JsonResponse

from ninja import Router, Schema

router = Router()


class Error(Schema):
    message: str


@router.get("/dapau", response={500: Error})
def dapau(request):
    raise Exception("break on purpose")


@router.get("/status")
def status(request):
    cursor = connection.cursor()
    cursor.execute("""SELECT 1+1""")
    row = cursor.fetchone()
    git_hash = os.getenv("GIT_HASH", "?")
    return JsonResponse(
        {
            "status": "ok",
            "db": "ok" if row == (2,) else "error",
            "git_hash": git_hash,
        }
    )
