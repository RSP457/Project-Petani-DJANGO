from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profil/', views.daftar_petani, name='daftar_petani'),
    path('profil/<int:id>/', views.detail_petani, name='detail_petani'),
    path('peta/', views.peta, name='peta'),
    path('produk/', views.produk_list, name='produk'),
]

