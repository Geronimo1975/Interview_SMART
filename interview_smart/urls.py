# interview_smart/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Lista de URL-uri simplificată pentru început
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Adăugăm configurația pentru fișierele media dacă suntem în modul de dezvoltare
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)