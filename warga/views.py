from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from .models import Warga, Pengaduan
from rest_framework import viewsets
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, filters
from .models import Warga
from .serializers import WargaSerializer

# ================================
#   VIEW BIASA (HTML)
# ================================

# 1. Daftar semua warga (HTML)
def warga_list(request):
    warga = Warga.objects.all()
    return render(request, 'warga/warga_list.html', {'warga': warga})

# 2. Detail warga (HTML)
def warga_detail(request, pk):
    warga = get_object_or_404(Warga, pk=pk)
    pengaduan = Pengaduan.objects.filter(warga=warga)
    return render(request, 'warga/warga_detail.html', {
        'warga': warga,
        'pengaduan': pengaduan
    })

# 3. Tambah warga (HTML)
def tambah_warga(request):
    if request.method == 'POST':
        nama = request.POST.get('nama_lengkap')
        alamat = request.POST.get('alamat')
        tanggal_lahir = request.POST.get('tanggal_lahir')

        Warga.objects.create(
            nama_lengkap=nama,
            alamat=alamat,
            tanggal_lahir=tanggal_lahir
        )
        return redirect('warga_list')

    return render(request, 'warga/tambah_warga.html')

# 4. Tambah pengaduan (HTML)
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

# 5. Edit warga (HTML)
def edit_warga(request, pk):
    warga = get_object_or_404(Warga, pk=pk)

    if request.method == 'POST':
        warga.nama_lengkap = request.POST.get('nama_lengkap')
        warga.alamat = request.POST.get('alamat')
        warga.tanggal_lahir = request.POST.get('tanggal_lahir')
        warga.save()
        return redirect('warga_detail', pk=warga.pk)

    return render(request, 'warga/edit_warga.html', {'warga': warga})

# 6. Hapus warga (HTML)
def hapus_warga(request, pk):
    warga = get_object_or_404(Warga, pk=pk)

    if request.method == 'POST':
        warga.delete()
        return redirect('warga_list')

    return render(request, 'warga/konfirmasi_hapus.html', {'warga': warga})


# ================================
#   API (JSON)
# ================================

# === GET + POST → /warga/api/
@csrf_exempt
def api_daftar_warga(request):
    # GET: semua data warga
    if request.method == "GET":
        warga_list = list(Warga.objects.all().values(
            "id", "nama_lengkap", "alamat", "tanggal_lahir"
        ))
        return JsonResponse({"warga": warga_list})

    # POST: tambah warga baru
    if request.method == "POST":
        data = json.loads(request.body)
        warga = Warga.objects.create(
            nama_lengkap=data["nama_lengkap"],
            alamat=data["alamat"],
            tanggal_lahir=data["tanggal_lahir"],
        )
        return JsonResponse({"message": "Warga ditambahkan", "id": warga.id})

    return JsonResponse({"error": "Method not allowed"}, status=405)


# === GET + PUT + DELETE → /warga/api/<pk>/
@csrf_exempt
def api_warga_detail(request, pk):
    # Cek apakah warga ada
    warga = get_object_or_404(Warga, pk=pk)

    # GET: detail warga
    if request.method == "GET":
        return JsonResponse({
            "id": warga.id,
            "nama_lengkap": warga.nama_lengkap,
            "alamat": warga.alamat,
            "tanggal_lahir": warga.tanggal_lahir,
        })

    # PUT: update warga
    if request.method == "PUT":
        data = json.loads(request.body)
        warga.nama_lengkap = data.get("nama_lengkap", warga.nama_lengkap)
        warga.alamat = data.get("alamat", warga.alamat)
        warga.tanggal_lahir = data.get("tanggal_lahir", warga.tanggal_lahir)
        warga.save()
        return JsonResponse({"message": "Warga diupdate"})

    # DELETE: hapus warga
    if request.method == "DELETE":
        warga.delete()
        return JsonResponse({"message": "Warga dihapus"})

    return JsonResponse({"error": "Method not allowed"}, status=405)

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

    # 🔎 Searching
    search_fields = ['nama_lengkap', 'alamat', 'tanggal_lahir']

    # ↕ Ordering
    ordering_fields = ['id', 'nama_lengkap', 'tanggal_lahir']
    ordering = ['id']  # default urutan

class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]

def warga_list_page(request):
    warga = Warga.objects.all().order_by('id')
    return render(request, 'warga/warga_list_page.html', {'warga': warga})

def warga_page(request):
    return render(request, "warga/index.html")

