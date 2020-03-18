"""work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boya import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ana_sayfa, name="home"),
    path('ajax/validate_username/', views.validate_username, name="degis"),
    path('ajax/not_ekle/', views.not_ekle, name="ekle"),
    path('defter/', views.borc_defteri, name="defter"),
    path('defter/defterler/<id>', views.borc_defteri_id, name="defter_ayrinti"),
    path('defter/ekle', views.borc_defteri_ekle, name="defter_ekle"),
    path('defter/<id>/sil/', views.borc_defteri_sil, name="defter_sil"),
    path('boyacilar/', views.boyacilar, name="boyacilar"),
    path('boyaci/<id>/detay', views.boyaci_ayrinti, name="boyaci_ayrinti"),
    #path('boyaci/ekle', views.boyaci_ekle, name="boyaci_ekle"),
    #path('boyaci/<id>/sil', views.boyaci_ekle, name="boyaci_sil"),

]
