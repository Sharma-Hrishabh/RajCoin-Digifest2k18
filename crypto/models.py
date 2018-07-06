from __future__ import unicode_literals

from django.db import models

# Create your models here.

class blockDB(models.Model):
    data = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    previousHash = models.CharField(max_length = 40)
    currentBlock = models.CharField(max_length = 40)
    senderKey = models.CharField(max_length = 50)
    recieverKey = models.CharField(max_length = 50)
    description = models.TextField(default = 'NO DESCRIPTION')
