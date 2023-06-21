from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ("description", "keyword", "link")


admin.site.register(Link, LinkAdmin)
