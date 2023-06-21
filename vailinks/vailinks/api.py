from ninja import NinjaAPI
from ninja.security import django_auth

from ..base.views import router as base_router
from ..accounts.views import router as accounts_router
from ..core.views import router as core_router

api = NinjaAPI(csrf=True)

api.add_router("/", base_router, tags=["base"])
api.add_router("/accounts/", accounts_router, tags=["accounts"])
api.add_router("/core/", core_router, auth=django_auth, tags=["core"])
