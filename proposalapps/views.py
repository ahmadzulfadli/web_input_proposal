from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.views.generic.base import TemplateView

from proposalapps.models import ketProposal


from .forms import UserLogin, ketProposalForm

#-------------------------------------------------------------------------------------
#=================================registrasi==========================================
def login_page(request):
    if request.user.is_authenticated:
        return redirect('input')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('input')
            else:
                messages.info(request, 'Username Atau Password Salah')
    return render(request, 'user/login.html') 

def login_page1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('input')
        else:
            messages.info(request, 'Username Atau Password Salah')
    return render(request, 'user/login1.html') 

def registrasi(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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

def logout_page(request):
    logout(request)
    return redirect('home')

#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#====================================template=========================================
def home(request):
    jumlah = ketProposal.objects.count()

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
    
    print(contex['jmt'])

    return render(request, 'index.html', contex)

def pengajuan(request):
    if request.method == 'POST':
        proposal = ketProposalForm(request.POST, request.FILES)
        if proposal.is_valid():
            proposal.save()
            messages.success(request, "Proposal Telah Di Ajukan, Silahkan Tunggu Email Balasannya")
            return redirect('home')
        else:
             messages.success(request, "Proposal tidak terkirim")
    else:
        proposal = ketProposalForm()
       
    contex={
        'proposal':proposal,
    }

    return render(request, 'input.html', contex)

def panduan(request):
    contex={}

    return render(request, 'panduan.html', contex)

#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=====================================================================================
#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=====================================================================================
#=====================================================================================
#-------------------------------------------------------------------------------------