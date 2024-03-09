from django.contrib import admin

from .models import Workspace, Link


class LinkInline(admin.TabularInline):
    model = Link


class WorkspaceAdmin(admin.ModelAdmin):
    inlines = [
        LinkInline,
    ]


admin.site.register(Workspace, WorkspaceAdmin)
# admin.site.register(Link)
