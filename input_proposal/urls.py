from django.contrib import admin
from django.urls import path
from proposalapps.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('input/', pengajuan, name="input"),
    path('panduan/', panduan, name="panduan"),

    path('login/', login_page, name="login"),
    path('login1/', login_page1, name="login1"),
    path('logout/', logout_page, name="logout"),
    path('registrasi/', registrasi, name="registrasi"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)