from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
urlpatterns = staticfiles_urlpatterns()
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns += [
    url(r'^$',views.anasayfa),
    url(r'^hakkimizda/', views.hakkimizda),
    url(r'^iletisim/', views.iletisim),
    url(r'^ekle/', views.ekle),
    url(r'^listele/', views.listele),
    url(r'^videoSil/(\d+$)', views.videoSil),
    url(r'^ekleDevam/(\d+$)', views.ekleDevam),
    url(r'^videoAnahtarEkle/', views.videoAnahtarEkle),
    url(r'^videoAnahtarOlayEkle/', views.videoAnahtarOlayEkle),
    url(r'^ozelliklerListele/', views.ozelliklerListele),
    url(r'^olayOzelliklerListele/', views.olayOzelliklerListele),
    url(r'^videoAnahtarSil/(\d+$)', views.videoAnahtarSil),
    url(r'^attTypePage/', views.attTypePage), 
    url(r'^attTypeListele/', views.attTypeListele),
    url(r'^attTypeSil/(\d+$)', views.attTypeSil),
    url(r'^attTypeDuzenle/(\d+$)', views.attTypeDuzenle),
    url(r'^attTypeDuzenleme/', views.attTypeDuzenleme),
    url(r'^resimEkle/', views.resimEkle),
    url(r'^resimEkleme/', views.resimEkleme),
    url(r'^sVideoEkle/', views.sVideoEkle),
    #url(r'^sVideoSonuc/', views.sVideoSonuc),    
    #url(r'^yuzTanimaSonuc/', views.yuzTanimaSonuc),    
    url(r'^deneme/', views.deneme),
]
