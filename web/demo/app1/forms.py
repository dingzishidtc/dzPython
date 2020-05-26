#-*-coding:GBK -*-
from django import forms

class PersonForm(forms.Form):
    first_name = forms.CharField(label='你的名字',max_length=20)
    last_name = forms.CharField(label='你的姓氏',max_length=20)
