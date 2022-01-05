from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.http import FileResponse
from django.contrib.auth.models import User, Group
from django.db.models import Count

from .models import *
from .forms import *

#-------------------------------------------------------------------------------------
#=================================registrasi==========================================
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.groups.filter(name='wd3').exists():
                return redirect('wakilDekan')
            elif user.groups.filter(name='kaprodi').exists():
                return redirect('kaprodi')
            elif user.groups.filter(name='pengaju').exists():
                return redirect('input')
            else:
                return redirect('login')
        else:
            messages.info(request, 'Username Atau Password Salah')
    return render(request, 'user/login.html') 

def registrasi(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Akun Berhasil Di buat untuk ')
            return redirect('home')

    contex = {
        'form':form,
    }
    return render(request, 'user/registrasi.html', contex) 
#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#====================================template pengaju=========================================
def home(request):
    jumlah = ketProposal.objects.count()

    if(jumlah > 0):
        
        te = ketProposal.objects.filter(asal_instansi=1).count()
        tif = ketProposal.objects.filter(asal_instansi=2).count()
        tin = ketProposal.objects.filter(asal_instansi=3).count()
        sif = ketProposal.objects.filter(asal_instansi=4).count()
        mt = ketProposal.objects.filter(asal_instansi=5).count()
        sema = ketProposal.objects.filter(asal_instansi=6).count()
        dema = ketProposal.objects.filter(asal_instansi=7).count()
        lainnya = ketProposal.objects.filter(asal_instansi=8).count()

        contex = {
            'jsema':round(sema/jumlah*100),
            'jdema':round(dema/jumlah*100),
            'jte':round(te/jumlah*100),
            'jtif':round(tif/jumlah*100),
            'jtin':round(tin/jumlah*100),
            'jsif':round(sif/jumlah*100),
            'jmt':round(mt/jumlah*100),
            'jlainnya':round(lainnya/jumlah*100),

        }
    else:
        contex = {}

    return render(request, 'index.html', contex)

def panduan(request):
    contex={}

    return render(request, 'panduan.html', contex)

def pengajuan(request):
    if request.method == 'POST':
        proposal = ketProposalForm(request.POST, request.FILES)
        if proposal.is_valid():
            proposal.save()
            messages.success(request, "Proposal Telah Di Ajukan, Silahkan Tunggu Email Balasannya")
            return redirect('hasil_pengaju')
        else:
             messages.success(request, "Proposal tidak terkirim")
    else:
        proposal = ketProposalForm()
       
    contex={
        'proposal':proposal,
    }

    return render(request, 'input.html', contex)

def hasil_pengaju(request):
    
    contex={}

    return render(request, 'hasil_pengaju.html', contex)

#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=================================template wd3========================================
def wakilDekan(request):
    sema = ketProposal.objects.filter(asal_instansi=6).count()
    dema = ketProposal.objects.filter(asal_instansi=7).count()
    lainnya = ketProposal.objects.filter(asal_instansi=8).count()

    te = ketProposal.objects.filter(asal_instansi=1, keterangan=2)
    tif = ketProposal.objects.filter(asal_instansi=2, keterangan=2)
    tin = ketProposal.objects.filter(asal_instansi=3, keterangan=2)
    sif = ketProposal.objects.filter(asal_instansi=4, keterangan=2)
    mt = ketProposal.objects.filter(asal_instansi=5, keterangan=2)

    contex = {
        'sema':sema,
        'dema':dema,
        'te':te.count(),
        'tif':tif.count(),
        'tin':tin.count(),
        'sif':sif.count(),
        'mt':mt.count(),
        'lainnya':lainnya,
    }
    if request.method == 'POST':
        return redirect('listproposalwd3')

    return render(request, 'atasan/wd3.html', contex)

def listProposalwd3(request):
    model = None
    system = request.POST.get('system', None)
    if system == 'te':
        model = ketProposal.objects.filter(asal_instansi=1, keterangan=2)
    elif system == 'tif':
        model = ketProposal.objects.filter(asal_instansi=2, keterangan=2)
    elif system == 'tin':
        model = ketProposal.objects.filter(asal_instansi=3, keterangan=2)
    elif system == 'sif':
        model = ketProposal.objects.filter(asal_instansi=4, keterangan=2)
    elif system == 'mt':
        model = ketProposal.objects.filter(asal_instansi=5, keterangan=2)
    elif system == 'sema':
        model = ketProposal.objects.filter(asal_instansi=6)
    elif system == 'dema':
        model = ketProposal.objects.filter(asal_instansi=7)
    elif system == 'lainnya':
        model = ketProposal.objects.filter(asal_instansi=8)
    else:
        return redirect('listproposalwd3')

    contex = {
        'model':model,
    }

    return render(request, 'atasan/list_proposalwd3.html', contex)

def viewswd3(request, id):
    model = get_object_or_404(ketProposal, id=id)

    contex = {
        'model': model,
    }

    return render(request, 'atasan/viewswd3.html', contex)

#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=================================template kaprodi====================================
def kaprodi(request):
    #list proposal
    if request.user.groups.filter(name = 'te').exists():
        model = ketProposal.objects.filter(asal_instansi=1)
    elif request.user.groups.filter(name = 'tif').exists():
        model = ketProposal.objects.filter(asal_instansi=2)
    elif request.user.groups.filter(name = 'tin').exists():
        model = ketProposal.objects.filter(asal_instansi=3)
    elif request.user.groups.filter(name = 'sif').exists():
        model = ketProposal.objects.filter(asal_instansi=4)
    elif request.user.groups.filter(name = 'mt').exists():
        model = ketProposal.objects.filter(asal_instansi=5)
    else:
        print("error")

    contex = {
        'model':model,
    }

    return render(request, 'kaprodi/kaprodi.html', contex)

def viewskaprodi(request, id):
    model = get_object_or_404(ketProposal, id=id)
    if request.method == 'POST':
        proposal = statusForm(request.POST, request.FILES)
        if proposal.is_valid():
            proposal.save()
            messages.success(request, "Proposal Telah Di Ajukan, Silahkan Tunggu Email Balasannya")
            return redirect('hasil_pengaju')
        else:
             messages.success(request, "Proposal tidak terkirim")
    else:
        proposal = statusForm()

    contex = {
        'model': model,
    }

    return render(request, 'kaprodi/viewskaprodi.html', contex)
#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=====================================================================================
#=====================================================================================
#-------------------------------------------------------------------------------------