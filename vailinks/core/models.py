from django.db import models
from ..accounts.models import User


class Link(models.Model):
    description = models.CharField(max_length=512, null=True, blank=True)
    link = models.URLField(max_length=2048, unique=True, default="")
    keyword = models.CharField(max_length=64, unique=True, default="")

    def to_dict_json(self):
        return {
            "id": self.id,
            "keyword": self.keyword,
            "link": self.link,
            "description": self.description,
        }
