from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ("description", "done")


admin.site.register(Link, LinkAdmin)
