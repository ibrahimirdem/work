from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import Notlar, BorcDefteri, Boyaci, Etiket, VerilenIs
from .forms import NotEkleForm, DefterEkleForm, BoyaciEkleForm, VerilenIsEkleForm


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

def borc_defteri(request):
    defterler = BorcDefteri.objects.all()
    return render(request, 'defter.html', {'defterler': defterler})

def borc_defteri_duzenle(request, id):
    defter = BorcDefteri.objects.get(id=id)
    if request.method == "POST":
        forms = DefterEkleForm(request.POST, instance=defter)
        if forms.is_valid():
            forms.save()
            return redirect("defter")
    else:
        forms = DefterEkleForm(instance=defter)
    return render(request, 'borc_defteri_duzenle.html', {'forms':forms})

def borc_defteri_sil(request, id):
    borc_defteri = BorcDefteri.objects.get(id=id)
    borc_defteri.delete()
    return redirect('defter')

def borc_defteri_id(request, id):
    defter = BorcDefteri.objects.get(id=id)
    return render(request, 'defter_ayrinti.html', {'defter': defter})

def borc_defteri_ekle(request):
    if request.method == "POST":
        forms = DefterEkleForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('defter')
    else:
        forms = DefterEkleForm()
    return render(request, 'defter_ekle.html', {'forms':forms})

def boyaci_ayrinti(request, id):
    boyaci = Boyaci.objects.get(id=id)
    return render(request, 'boyaci_ayrinti.html', {'boyaci': boyaci})
    
def boyacilar(request):
    boyacilar = Boyaci.objects.all()
    return render(request, 'boyacilar.html',  {'boyacilar': boyacilar})

def boyaci_ekle(request):
    if request.method == "POST":
        forms = BoyaciEkleForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("boyacilar")
    else:
        forms = BoyaciEkleForm()
    return render(request, 'boyaci_ekle.html', {'forms':forms})

def boyaci_sil(request, id):
    boyaci = Boyaci.objects.get(id=id)
    boyaci.delete()
    return redirect("boyacilar")

def boyaci_duzenle(request, id):
    boyaci = Boyaci.objects.get(id=id)
    if request.method == "POST":
        forms = BoyaciEkleForm(request.POST, instance=boyaci)
        if forms.is_valid():
            forms.save()
            return redirect("boyacilar")
    else:
        forms = BoyaciEkleForm(instance=boyaci)
    return render(request, 'boyaci_duzenle.html', {'forms':forms})

def etiket(request, id):
    etiket = Etiket.objects.get(id=id)
    return render(request, 'etiket.html', {'etiket': etiket})

def isler(request):
    isler = VerilenIs.objects.all()
    return render(request, 'isler.html', {'isler': isler})

def is_ekle(request):
    if request.method == "POST":
        forms = VerilenIsEkleForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("isler")
    else:
        forms = VerilenIsEkleForm()
    return render(request, 'is_ekle.html', {'forms':forms})
    
