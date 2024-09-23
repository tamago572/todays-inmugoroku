from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Goroku(models.Model):
    goroku = models.CharField("語録", max_length=200, default="やりますねぇ！")
    author = models.CharField("人物", max_length=30, default="野獣先輩")
    age = models.IntegerField("年齢を教えてくれるかな", default=24)
    created_at = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.goroku
