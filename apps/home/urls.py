from django.conf.urls import url, include 
from apps.home.views import home

urlpatterns = [
    url(r'^$', home,name='home'),
]
