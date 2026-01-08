from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profil/', views.profil, name='profil'),
    path('peta/', views.peta, name='peta'),
    path('produk/', views.produk_list, name='produk'),
]
