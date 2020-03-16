from django import forms
from .models import Notlar

class NotEkleForm(forms.ModelForm):

    class Meta:
        model = Notlar
        fields = ['not_aciklama']
