from django.db import models


class ModelBase(models.Model):
    class Meta:
        abstract = True
        ordering = ["-created", ]

    created = models.DateTimeField("作成日時", auto_now_add=True)
    update = models.DateTimeField("更新日時", auto_now=True)
    enable = models.BooleanField("有効", default=True)
