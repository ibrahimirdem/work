from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Notlar
from .forms import NotEkleForm


# Create your views here.
def ana_sayfa(request):
    if request.method == "POST":
        forms = NotEkleForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms = NotEkleForm()
    notlar = Notlar.objects.all()
    return render(request, 'home.html', {'notlar':notlar, 'forms':forms})

def validate_username(request):
    numara = request.GET.get('numara', None)
    deger = request.GET.get('deger', None)
    notum =Notlar.objects.get(id=numara)
    if deger == "yapildi":
        notum.yapildi_mi = True
    else:
        notum.yapildi_mi = False
    notum.save()
    data = {'is_taken': 'merhabalar'}
    return JsonResponse(data)

def not_ekle(request):
    notum = request.GET.get('not', None)
    not_olustur = Notlar(not_aciklama=notum)
    not_olustur.save()

    data = {'id': not_olustur.id,
            'not_aciklama': not_olustur.not_aciklama,
            'yapildi_mi': not_olustur.yapildi_mi}
    return JsonResponse(data)