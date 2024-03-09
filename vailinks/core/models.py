from django.db import models
from vailinks.accounts.models import User


class Workspace(models.Model):
    name = models.CharField(max_length=64, unique=True, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
        }


class Link(models.Model):
    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE, blank=True, null=True
    )
    keyword = models.CharField(max_length=64, default="")
    link = models.URLField(max_length=2048, default="")
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        ordering = ["keyword"]

    def __str__(self):
        return self.keyword

    def to_dict_json(self):
        return {
            "id": self.id,
            "workspace_id": self.workspace_id,
            "keyword": self.keyword,
            "link": self.link,
            "description": self.description,
        }
