from django.db import models

# Create your models here.
class Etiket(models.Model):
    etiket_adi = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Etiket"
        verbose_name_plural = "Etiketler"

    def __str__(self):
        return self.etiket_adi

    
class Boyaci(models.Model):
    isim = models.CharField(max_length=100)
    telefon_no = models.CharField(max_length=11)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    aciklama = models.TextField()
    boyaci_etiket = models.ManyToManyField(Etiket, related_name="boyacilar")

    class Meta:
        verbose_name = "Boyacı"
        verbose_name_plural = "Boyacılar"

    def __str__(self):
        return self.isim


class VerilenIs(models.Model):
    is_alan_boyaci = models.ForeignKey(Boyaci, on_delete=models.CASCADE, 
                                        related_name="verilen_isler", verbose_name="Boyacı")
    is_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="İş Alma Tarihi")
    is_aciklama = models.TextField(verbose_name="Açıklama")

    class Meta:
        verbose_name = "Verilen İş"
        verbose_name_plural = "Verilen İşler"

    def __str__(self):
        return self.is_aciklama