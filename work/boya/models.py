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


class BorcDefteri(models.Model):
    borclu_isim = models.CharField(max_length=100, verbose_name="Borçlu İsmi")
    borclu_telefon = models.CharField(max_length=11, verbose_name="Telefon")
    borclu_aciklama = models.TextField(verbose_name="Açıklama")
    borc_baslangic = models.DateTimeField(auto_now_add=True)
    borc_son_odeme = models.DateTimeField(blank=True, null=True, verbose_name="Ödeme Tarihi")
    
    class Meta:
        verbose_name = "Borç Defteri"
        verbose_name_plural = "Borç Defteri"
    
    def __str__(self):
        return self.borclu_isim
    

class Notlar(models.Model):
    not_aciklama = models.TextField(verbose_name="Not Açıklaması")
    yapildi_mi = models.BooleanField(default=False, verbose_name="Yapıldı mı")
    not_tarihi = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        verbose_name = "Not"
        verbose_name_plural = "Notlar"

    def __str__(self):
        return self.not_aciklama
    