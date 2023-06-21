"""Django ninja URLs"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", TemplateView.as_view(template_name="base/apihome.html")),
]
