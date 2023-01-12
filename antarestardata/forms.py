from django.forms import ModelForm
from antarestardata.models import *
from django import forms

class FormPreorder(ModelForm):
    class Meta:
        model=Preorder
        fields = "__all__"