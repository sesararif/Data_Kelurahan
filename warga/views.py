# warga/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Warga, Pengaduan
from django.utils import timezone

# === 1. Daftar semua warga ===
def warga_list(request):
    warga = Warga.objects.all()
    return render(request, 'warga/warga_list.html', {'warga': warga})

# === 2. Detail data 1 warga ===
def warga_detail(request, pk):
    warga = get_object_or_404(Warga, pk=pk)
    pengaduan = Pengaduan.objects.filter(warga=warga)
    return render(request, 'warga/warga_detail.html', {
        'warga': warga,
        'pengaduan': pengaduan
    })

# === 3. Tambah warga baru ===
def tambah_warga(request):
    if request.method == 'POST':
        nama = request.POST.get('nama_lengkap')
        alamat = request.POST.get('alamat')
        tanggal_lahir = request.POST.get('tanggal_lahir')

        # Simpan ke database
        Warga.objects.create(
            nama_lengkap=nama,
            alamat=alamat,
            tanggal_lahir=tanggal_lahir
        )
        return redirect('warga_list')

    return render(request, 'warga/tambah_warga.html')

# === 4. Tambah pengaduan baru ===
def tambah_pengaduan(request):
    if request.method == 'POST':
        warga_id = request.POST.get('warga')
        isi = request.POST.get('isi_pengaduan')

        warga = get_object_or_404(Warga, id=warga_id)
        Pengaduan.objects.create(
            warga=warga,
            isi_pengaduan=isi,
            tanggal=timezone.now()
        )
        return redirect('warga_detail', pk=warga.id)

    warga = Warga.objects.all()
    return render(request, 'warga/tambah_pengaduan.html', {'warga': warga})

# === 5. Edit warga ===
def edit_warga(request, pk):
    warga = get_object_or_404(Warga, pk=pk)

    if request.method == 'POST':
        warga.nama_lengkap = request.POST.get('nama_lengkap')
        warga.alamat = request.POST.get('alamat')
        warga.tanggal_lahir = request.POST.get('tanggal_lahir')
        warga.save()
        return redirect('warga_detail', pk=warga.pk)

    return render(request, 'warga/edit_warga.html', {'warga': warga})


# === 6. Hapus warga ===
def hapus_warga(request, pk):
    warga = get_object_or_404(Warga, pk=pk)

    if request.method == 'POST':
        warga.delete()
        return redirect('warga_list')

    return render(request, 'warga/konfirmasi_hapus.html', {'warga': warga})
