from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Notlar


# Create your views here.
def ana_sayfa(request):
    notlar = Notlar.objects.all()
    return render(request, 'home.html', {'notlar':notlar})

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