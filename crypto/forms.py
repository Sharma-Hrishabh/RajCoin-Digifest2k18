from django import forms
from . import blockchain
from . import models

class SellBlock(forms.ModelForm):
    class Meta:
        model = models.testblockDB
        fields = ['data','amount','senderKey','receiverKey']
