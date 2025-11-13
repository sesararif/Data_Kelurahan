from django.urls import path
from . import views

urlpatterns = [
    path('', views.warga_list, name='warga_list'),
    path('<int:pk>/', views.warga_detail, name='warga_detail'),
    path('tambah/', views.tambah_warga, name='tambah_warga'),
    path('pengaduan/', views.tambah_pengaduan, name='tambah_pengaduan'),
    path('<int:pk>/edit/', views.edit_warga, name='edit_warga'),
    path('<int:pk>/hapus/', views.hapus_warga, name='hapus_warga'),
]





