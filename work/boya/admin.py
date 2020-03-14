from django.contrib import admin
from .models import Boyaci, Etiket, VerilenIs, BorcDefteri, Notlar

# Register your models here.
class BoyaciAdmin(admin.ModelAdmin):
    list_display = ['isim', 'telefon_no', 'aciklama']
    search_fields = ['isim', 'telefon_no', 'aciklama']

    class Meta:
        model = Boyaci

class VerilenIsAdmin(admin.ModelAdmin):
    model = VerilenIs
    
    list_display = ['isi_alan','is_aciklama']

    def isi_alan(self, obj):
        return obj.is_alan_boyaci.isim
    isi_alan.admin_order_field  = 'is_alan_boyaci'
    
class BorcDefteriAdmin(admin.ModelAdmin):
    model = BorcDefteri

    list_display = ["borclu_isim", "borclu_telefon", "borclu_aciklama", "borc_son_odeme"]
    search_fields = ["borclu_isim", "borclu_telefon", "borclu_aciklama"]

class NotlarAdmin(admin.ModelAdmin):
    model = Notlar

    list_display = ["not_aciklama", "yapildi_mi", "not_tarihi"]

admin.site.register(Boyaci, BoyaciAdmin)
admin.site.register(Etiket)
admin.site.register(VerilenIs, VerilenIsAdmin)
admin.site.register(BorcDefteri, BorcDefteriAdmin)
admin.site.register(Notlar, NotlarAdmin)
