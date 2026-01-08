from django.db import models

class ProfilPetani(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='profil/')

    def __str__(self):
        return self.nama


class DetailPetani(models.Model):
    nama = models.CharField(max_length=150)
    alamat = models.TextField()
    whatsapp = models.CharField(max_length=20)
    komoditas = models.CharField(max_length=100)
    riwayat = models.TextField()

    def __str__(self):
        return self.nama


class Lahan(models.Model):
    nama_petani = models.CharField(max_length=100)
    alamat = models.TextField()
    tanaman = models.CharField(max_length=100)
    luas = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nama_petani

class Produk(models.Model):
    nama_produk = models.CharField(max_length=100)
    stok = models.CharField(max_length=50, default="Masih proses tanam")
    harga = models.CharField(max_length=50, default="-")
    foto = models.ImageField(upload_to='produk/', blank=True, null=True)

    def __str__(self):
        return self.nama_produk

