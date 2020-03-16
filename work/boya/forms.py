from django import forms
from .models import Notlar

class NotEkleForm(forms.ModelForm):

    class Meta:
        model = Notlar
        fields = ('not_aciklama',)
        #help_texts = {'not_aciklama': ('Enter a date between now and 4 weeks (default 3).')} 
        labels = {'not_aciklama': ('Not:')}