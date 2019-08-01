from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import bank_detail
from django.conf.urls import include


urlpatterns = [
	 url(r'^', include('fyleApp.urls')),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
	url(r'^admin/', admin.site.urls),
    
]
