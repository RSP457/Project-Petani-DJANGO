from django.db import models

# PROFIL UTAMA PETANI
class ProfilPetani(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='profil/', blank=True, null=True)

    def __str__(self):
        return self.nama
class DetailPetani(models.Model):
    profil = models.OneToOneField(
        ProfilPetani,
        on_delete=models.CASCADE,
        related_name='detail'
    )
    alamat = models.TextField()
    whatsapp = models.CharField(max_length=20)
    komoditas = models.CharField(max_length=100)
    riwayat = models.TextField()

    def __str__(self):
        return f"Detail {self.profil.nama}"

# LAHAN PETANI (1–N)

class Lahan(models.Model):
    petani = models.ForeignKey(
        ProfilPetani,
        on_delete=models.CASCADE,
        related_name='lahan',
        null=True,
        blank=True
    )
    alamat = models.TextField()
    tanaman = models.CharField(max_length=100)
    luas = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.petani.nama if self.petani else '-'} - {self.tanaman}"
# HASIL PANEN (1–N)
class HasilPanen(models.Model):
    petani = models.ForeignKey(
        ProfilPetani,
        on_delete=models.CASCADE,
        related_name='hasil_panen'
    )
    nama_panen = models.CharField(max_length=100)
    jumlah = models.FloatField(help_text="Dalam Kg")
    tanggal_panen = models.DateField()
    keterangan = models.TextField(blank=True)
    foto = models.ImageField(
        upload_to='hasil_panen/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nama_panen} - {self.petani.nama}"

# PRODUK
class Produk(models.Model):
    petani = models.ForeignKey(
        ProfilPetani,
        on_delete=models.CASCADE,
        related_name='produk',
        null=True,
        blank=True
    )
    hasil_panen = models.ForeignKey(
        HasilPanen,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    nama_produk = models.CharField(max_length=100)
    stok = models.CharField(max_length=50, default="Masih proses tanam")
    harga = models.CharField(max_length=50, default="-")
    foto = models.ImageField(upload_to='produk/', blank=True, null=True)

    def __str__(self):
        return self.nama_produk
