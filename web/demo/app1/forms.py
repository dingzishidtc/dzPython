#-*-coding:GBK -*-
from django import forms

class PersonForm(forms.Form):
    first_name = forms.CharField(label='�������',max_length=20)
    last_name = forms.CharField(label='�������',max_length=20)
