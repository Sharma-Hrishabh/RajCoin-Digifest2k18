from django import forms
from . import blockchain
from . import models

class SellBlock(forms.ModelForm):
    class Meta:
        model = models.blockDB
        fields = ['data','amount','senderKey','receiverKey']
