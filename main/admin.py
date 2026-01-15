from django.contrib import admin
from .models import (
    ProfilPetani,
    DetailPetani,
    Lahan,
    HasilPanen,
    Produk
)

class DetailPetaniInline(admin.StackedInline):
    model = DetailPetani
    extra = 0
    max_num = 1
class LahanInline(admin.TabularInline):
    model = Lahan
    extra = 1
class HasilPanenInline(admin.TabularInline):
    model = HasilPanen
    extra = 1
    fields = ('nama_panen', 'jumlah', 'tanggal_panen', 'foto', 'keterangan')
class ProdukInline(admin.TabularInline):
    model = Produk
    extra = 1

# Admin Utama
@admin.register(ProfilPetani)
class ProfilPetaniAdmin(admin.ModelAdmin):
    list_display = ('nama',)
    search_fields = ('nama',)
    inlines = [
        DetailPetaniInline,
        LahanInline,
        HasilPanenInline,
        ProdukInline
    ]
