from django.shortcuts import render
from .models import ProfilPetani, DetailPetani, Lahan, Produk

def index(request):
    produk = Produk.objects.all()
    return render(request, 'main/index.html', {
        'produk': produk
    })


def profil(request):
    petani = DetailPetani.objects.first()
    return render(request, 'main/profil.html', {'petani': petani})


def peta(request):
    lahan = Lahan.objects.first()
    return render(request, 'main/peta.html', {'lahan': lahan})


def produk_list(request):
    produk = Produk.objects.all()
    return render(request, 'main/produk.html', {'produk': produk})
