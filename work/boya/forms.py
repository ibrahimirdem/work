from django import forms
from .models import Notlar, BorcDefteri

class NotEkleForm(forms.ModelForm):

    class Meta:
        model = Notlar
        fields = ('not_aciklama',)
        #help_texts = {'not_aciklama': ('Enter a date between now and 4 weeks (default 3).')} 
        labels = {'not_aciklama': ('Not:')}

class DefterEkleForm(forms.ModelForm):

    class Meta:
        model = BorcDefteri
        fields = ('borclu_isim', 'borclu_aciklama', 'borclu_telefon', 'borc_son_odeme',)