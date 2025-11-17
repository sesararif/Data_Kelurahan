from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from warga.views import WargaViewSet, PengaduanViewSet


router = routers.DefaultRouter()
router.register(r'warga', WargaViewSet)
router.register(r'pengaduan', PengaduanViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),  # Mengarah ke aplikasi warga
    path('', include('warga.urls')), 
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'), 
    path('api/', include(router.urls)),
]