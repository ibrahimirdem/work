from django.contrib import admin
from .models import Boyaci, Etiket, VerilenIs

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
    


admin.site.register(Boyaci, BoyaciAdmin)
admin.site.register(Etiket)
admin.site.register(VerilenIs, VerilenIsAdmin)

