from django.db import models


class Tutorials(models.Model):
    title = models.CharField(max_length=70, blank=True, default="")
    description = models.CharField(max_length=200, blank=True, default="")
    published = models.BooleanField(default=False)
