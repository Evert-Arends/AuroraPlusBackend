from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Servers(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Data = models.TextField()
