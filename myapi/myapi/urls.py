from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', admin.site.urls),
]