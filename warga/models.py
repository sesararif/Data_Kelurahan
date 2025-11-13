# warga/models.py
from django.db import models

class Warga(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    alamat = models.TextField()
    tanggal_lahir = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nama_lengkap


class Pengaduan(models.Model):
    warga = models.ForeignKey(Warga, on_delete=models.CASCADE)
    isi_pengaduan = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pengaduan oleh {self.warga.nama_lengkap}"
