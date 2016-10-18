from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Servers(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, default='No Name')
    ServerKey = models.TextField(max_length=200, default=0)


class ServerData(models.Model):
    ID = models.AutoField(primary_key=True)
    JsonData = models.TextField()
    ServerKey = models.TextField(max_length=200, default=0)
    Date = models.DateTimeField(auto_now_add=True)



