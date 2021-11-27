from django.shortcuts import render
from apps.forms import *

#=================================registrasi==========================================
def login(request):
    contex={}

    return render(request, 'user/login.html', contex) 

def registrasi(request):
    contex={}

    return render(request, 'user/registrasi.html', contex) 

def logout(request):
    contex={}

    return render(request, 'user/logout.html', contex) 
#=====================================================================================

#====================================template=========================================
def home(request):
    contex = {}

    return render(request, 'index.html', contex)

def pengajuan(request):
    proposal = dataUserForm()
    contex={
        'proposal':proposal
    }

    return render(request, 'input.html', contex)

def panduan(request):
    contex={}

    return render(request, 'panduan.html', contex)
#=====================================================================================

#=====================================================================================
#=====================================================================================

#=====================================================================================
#=====================================================================================