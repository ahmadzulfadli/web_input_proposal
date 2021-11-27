from django.contrib import admin
from django.urls import path
from apps.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('input/', pengajuan, name="input"),
    path('panduan/', panduan, name="panduan"),

    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('registrasi/', registrasi, name="registrasi"),
]
