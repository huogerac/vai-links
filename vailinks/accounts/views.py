# coding: utf-8
import logging
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ninja import Router, Form

from .schemas import LoggedUserSchema, UserSchema


logger = logging.getLogger(__name__)
router = Router()


@router.post("/login", response=UserSchema)
@csrf_exempt
def login(request, username: str = Form(...), password: str = Form(...)):
    username = request.POST["username"]
    password = request.POST["password"]
    logger.info(f"API login: {username}")
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            user_dict = _user2dict(user)
            logger.info(f"API login: {username} success")
    return JsonResponse(user_dict, safe=False)


@router.post("/logout")
def logout(request):
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    logger.info(f"API logout: {request.user.username}")
    auth.logout(request)
    return JsonResponse({})


@router.get("/whoami", response=LoggedUserSchema)
def whoami(request):
    i_am = (
        {
            "user": _user2dict(request.user),
            "authenticated": True,
        }
        if request.user.is_authenticated
        else {"authenticated": False}
    )
    logger.info("API whoami")
    return JsonResponse(i_am)


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "avatar": user.avatar,
        "bio": user.bio,
        "permissions": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        },
    }
    return d
