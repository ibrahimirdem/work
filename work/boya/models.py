from django.db import models

# Create your models here.
class Etiket(models.Model):
    etiket_adi = models.CharField(max_length=100)

    def __str__(self):
        return self.etiket_adi
    

class Boyaci(models.Model):
    isim = models.CharField(max_length=100)
    telefon_no = models.CharField(max_length=11)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    aciklama = models.TextField()
    boyaci_etiket = models.ManyToManyField(Etiket, related_name="boyacilar")

    def __str__(self):
        return self.isim


