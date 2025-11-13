from django.contrib import admin
from .models import Warga, Pengaduan

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'alamat', 'tanggal_lahir')
    search_fields = ('nama_lengkap', 'alamat')

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    list_display = ('id', 'warga', 'isi_pengaduan', 'tanggal')
    search_fields = ('warga__nama_lengkap', 'isi_pengaduan')

