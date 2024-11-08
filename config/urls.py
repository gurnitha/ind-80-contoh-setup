# config/urls.py

# Modul Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# Modul saya
from app.main import views # baru


urlpatterns = [
    # main
    path('', views.halodunia), # baru
    # admin
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)