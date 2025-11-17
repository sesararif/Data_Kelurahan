from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')

urlpatterns = [
    # HTML
    path('', views.warga_list, name='warga_list'),
    path('<int:pk>/', views.warga_detail, name='warga_detail'),
    path('tambah/', views.tambah_warga, name='tambah_warga'),
    path('pengaduan/', views.tambah_pengaduan, name='tambah_pengaduan'),
    path('<int:pk>/edit/', views.edit_warga, name='edit_warga'),
    path('<int:pk>/hapus/', views.hapus_warga, name='hapus_warga'),

    # API
    path('api/', views.api_daftar_warga, name='api_daftar_warga'),
    path('api/<int:pk>/', views.api_warga_detail, name='api_warga_detail'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]






