from django.db import models

from associations.models.association import Association
from authentication.models import User


class Page(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200)
    association = models.ForeignKey(Association, on_delete=models.CASCADE, related_name="pages")
    text = models.TextField(blank=True, null=True, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class File(models.Model):
    id = models.AutoField(primary_key=True)

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    file = models.FileField()
