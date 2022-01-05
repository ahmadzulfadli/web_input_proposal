from django.contrib import admin
from django.urls import path
from proposalapps.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('input/', pengajuan, name="input"),
    path('panduan/', panduan, name="panduan"),
    path('hasil_pengaju/', hasil_pengaju, name="hasil_pengaju"),
    path('wakilDekan/', wakilDekan, name="wakilDekan"),
    path('listproposalwd3/', listProposalwd3, name="listproposalwd3"),
    path('viewswd3/<str:id>/', viewswd3, name="viewswd3"),
    path('kaprodi/', kaprodi, name="kaprodi"),
    path('viewskaprodi/<str:id>/', viewskaprodi, name="viewskaprodi"),

    path('login/', login_page, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('registrasi/', registrasi, name="registrasi"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)