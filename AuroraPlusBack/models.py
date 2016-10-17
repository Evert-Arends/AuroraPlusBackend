from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Servers(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, default='No Name')

    Server_Key = models.TextField(max_length=200, default=0)


class ServerData(models.Model):
    ID = models.AutoField(primary_key=True)
    Data = models.TextField(max_length=255)
    Owner = models.TextField(max_length=255)
    CPU_Usage = models.TextField(max_length=20, default=0)
    NetworkLoad_Sent = models.IntegerField(default=0)
    NetworkLoad_Received = models.IntegerField(default=0)
    Server_Key = models.TextField(primary_key=True, max_length=200, default=0)


