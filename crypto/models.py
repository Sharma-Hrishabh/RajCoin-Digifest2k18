from __future__ import unicode_literals

from django.db import models

# Create your models here.

class blockDB(models.Model):
    data            = models.TextField(default = "")
    time            = models.DateTimeField(auto_now_add=True)
    previousHash    = models.CharField(max_length = 40)
    hashe           = models.CharField(max_length = 40)
    senderKey       = models.CharField(max_length = 50)
    receiverKey     = models.CharField(max_length = 50)
    amount          = models.FloatField(default = 0.0)

