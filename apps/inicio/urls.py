from django.conf.urls import url, include 
from apps.inicio.views import inicio

urlpatterns = [
    url(r'^$', inicio,name='inicio'),
]
