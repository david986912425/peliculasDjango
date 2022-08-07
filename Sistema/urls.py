from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    
    path('',views.inicio, name='inicio'),
    path('detalles/<slug>', views.detalles, name='detalles'),
    path('series', views.series, name='series'),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)