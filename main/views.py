from django.shortcuts import render
from .models import ProfilPetani, Lahan, Produk
from django.shortcuts import render, get_object_or_404


def index(request):
    produk = Produk.objects.all()
    return render(request, 'main/index.html', {'produk': produk})

def daftar_petani(request):
    petani_list = ProfilPetani.objects.all()
    return render(request, 'main/daftar_petani.html', {
        'petani_list': petani_list
    })

def detail_petani(request, id):
    petani = get_object_or_404(ProfilPetani, id=id)
    return render(request, 'main/profil.html', {
        'petani': petani
    })

def peta(request):
    lahan = Lahan.objects.first()
    return render(request, 'main/peta.html', {'lahan': lahan})

def produk_list(request):
    # AMBIL SEMUA DATA PRODUK DARI DATABASE
    produk = Produk.objects.all()

    return render(request, 'main/produk.html', {
        'produk': produk
    })
