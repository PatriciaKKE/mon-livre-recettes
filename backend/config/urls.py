
from django.contrib import admin
from django.urls import path, include
import django_prometheus.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prometheus/', include(django_prometheus.urls)),
    path('api/', include('livrerecettes_app.urls')),
]
