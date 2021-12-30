from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Group

from proposalapps.models import ketProposal

from .forms import UserLogin, ketProposalForm

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
        sema = ketProposal.objects.filter(asal_instansi="SEMA").count()
        dema = ketProposal.objects.filter(asal_instansi="DEMA").count()
        te = ketProposal.objects.filter(asal_instansi="Teknik Elektro").count()
        tif = ketProposal.objects.filter(asal_instansi="Teknik Informatika").count()
        tin = ketProposal.objects.filter(asal_instansi="Teknik Industri").count()
        sif = ketProposal.objects.filter(asal_instansi="Sistem Informasi").count()
        mt = ketProposal.objects.filter(asal_instansi="Matematika").count()
        lainnya = ketProposal.objects.filter(asal_instansi="Lainnya").count()

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
    sema = ketProposal.objects.filter(asal_instansi="SEMA").count()
    dema = ketProposal.objects.filter(asal_instansi="DEMA").count()
    te = ketProposal.objects.filter(asal_instansi="Teknik Elektro").count()
    tif = ketProposal.objects.filter(asal_instansi="Teknik Informatika").count()
    tin = ketProposal.objects.filter(asal_instansi="Teknik Industri").count()
    sif = ketProposal.objects.filter(asal_instansi="Sistem Informasi").count()
    mt = ketProposal.objects.filter(asal_instansi="Matematika").count()
    lainnya = ketProposal.objects.filter(asal_instansi="Lainnya").count()

    if request.method == 'POST' and 'te' in request.POST:
        print("teknik elektro")
        return redirect('listproposalwd3')

    elif request.method == 'POST' and 'tif' in request.POST:
        print("teknik informatika")
        return redirect('listproposalwd3')

    elif request.method == 'POST' and 'tin' in request.POST:
        print("teknik industri")
        return redirect('listproposalwd3')

    elif request.method == 'POST' and 'sif' in request.POST:
        print("sistem informasi")

    elif request.method == 'POST' and 'mt' in request.POST:
        print("matematika")

    elif request.method == 'POST' and 'sema' in request.POST:
        print("sema")

    elif request.method == 'POST' and 'dema' in request.POST:
        print("dema")

    elif request.method == 'POST' and 'lainnya' in request.POST:
        print("lainnya")
        
    else:
        print("error")

    contex = {
        'sema':sema,
        'dema':dema,
        'te':te,
        'tif':tif,
        'tin':tin,
        'sif':sif,
        'mt':mt,
        'lainnya':lainnya,
    }

    return render(request, 'atasan/wd3.html', contex)

def listProposalwd3(request):
    if request.method == 'POST' and 'te' in request.POST:
        print("teknik elektro")
        proposal = ketProposal.objects.filter(asal_instansi="Teknik Elektro")
        return proposal
    elif request.method == 'POST' and 'tif' in request.POST:
        print("teknik informatika")
        proposal = ketProposal.objects.filter(asal_instansi="Teknik Informatika")
        return proposal
    elif request.method == 'POST' and 'tin' in request.POST:
        print("teknik industri")
        proposal = ketProposal.objects.filter(asal_instansi="Teknik Industri")
        return proposal
    elif request.method == 'POST' and 'sif' in request.POST:
        print("sistem informasi")
    elif request.method == 'POST' and 'mt' in request.POST:
        print("matematika")
    elif request.method == 'POST' and 'sema' in request.POST:
        print("sema")
    elif request.method == 'POST' and 'dema' in request.POST:
        print("dema")
    elif request.method == 'POST' and 'lainnya' in request.POST:
        print("lainnya")
    else:
        print("error")

    contex = {
    }

    return render(request, 'atasan/list_proposalwd3.html', contex)

def viewswd3(request):
    contex = {}

    return render(request, 'atasan/viewswd3.html', contex)

#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=================================template kaprodi====================================
def kaprodi(request):
    contex = {}

    return render(request, 'kaprodi/kaprodi.html', contex)

def viewskaprodi(request):
    contex = {}

    return render(request, 'kaprodi/viewskaprodi.html', contex)
#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=====================================================================================
#=====================================================================================
#-------------------------------------------------------------------------------------