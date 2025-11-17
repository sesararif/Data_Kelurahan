from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),  # Mengarah ke aplikasi warga
    path('', include('warga.urls')), 
]