from django import forms
from . import blockchain


class SellBlock(forms.ModelForm):
    class Meta:
        model = models.block
        fields = ['data','amount','sender','receiver']
