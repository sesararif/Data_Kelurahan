from django.views.generic import ListView, DetailView
from .models import Warga

# View untuk menampilkan daftar warga
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'  # Opsional: eksplisit tentukan template
    context_object_name = 'object_list'     # Opsional: default sudah benar

# View untuk menampilkan detail satu warga
class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'object'  # default, bisa diubah jika ingin
