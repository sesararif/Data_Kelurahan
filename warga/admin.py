from django.contrib import admin
from .models import Warga

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nik', 'nama_lengkap', 'alamat', 'no_telepon', 'tanggal_registrasi')
    search_fields = ('nama_lengkap', 'nik')
    list_filter = ('tanggal_registrasi',)
