from django import forms
from .models import *


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = "__all__"

class expanseForm(forms.ModelForm):
    class Meta:
        model = Expanse
        fields = "__all__"


class expanseEditForm(forms.ModelForm):
    class Meta:
        model = Expanse
        fields = ['Amount']
