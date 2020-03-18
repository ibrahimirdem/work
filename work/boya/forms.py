from django import forms
from .models import Notlar, BorcDefteri, Boyaci, Etiket
from django.forms.widgets import CheckboxSelectMultiple


class NotEkleForm(forms.ModelForm):

    class Meta:
        model = Notlar
        fields = ('not_aciklama',)
        #help_texts = {'not_aciklama': ('Enter a date between now and 4 weeks (default 3).')} 
        #labels = {'not_aciklama': ('Not:')}

class DefterEkleForm(forms.ModelForm):

    class Meta:
        model = BorcDefteri
        fields = ('borclu_isim', 'borclu_aciklama', 'borclu_telefon', 'borc_son_odeme',)

class BoyaciEkleForm(forms.ModelForm):

    class Meta:
        model = Boyaci
        fields = ('isim', 'telefon_no', 'aciklama', 'boyaci_etiket',)
    
    def __init__(self, *args, **kwargs):
        
        super(BoyaciEkleForm, self).__init__(*args, **kwargs)
        
        self.fields["boyaci_etiket"].widget = CheckboxSelectMultiple()
        self.fields["boyaci_etiket"].queryset = Etiket.objects.all()
