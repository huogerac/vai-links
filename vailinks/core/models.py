from django.db import models
from ..accounts.models import User


class Link(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "done": self.done,
        }
