from django.shortcuts import render
from .models import ProfilPetani, DetailPetani, Lahan, Produk

def index(request):
    produk = Produk.objects.all()
    return render(request, 'main/index.html', {'produk': produk})


def profil(request):
    petani = DetailPetani.objects.first()
    return render(request, 'main/profil.html', {'petani': petani})


def peta(request):
    lahan = Lahan.objects.first()
    return render(request, 'main/peta.html', {'lahan': lahan})


from django.shortcuts import render
from .models import Produk

def produk_list(request):
    # AMBIL SEMUA DATA PRODUK DARI DATABASE
    produk = Produk.objects.all()

    return render(request, 'main/produk.html', {
        'produk': produk
    })
