from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ("description", "link", "keyword")


admin.site.register(Link, LinkAdmin)
