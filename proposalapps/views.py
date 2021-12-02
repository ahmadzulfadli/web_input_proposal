from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from proposalapps.models import ketProposal


from .forms import UserLogin, ketProposalForm
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

def registrasi(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun Berhasil Dibuat')
            return redirect('login')
    contex={
        'form':form,
    }

    return render(request, 'user/registrasi.html', contex) 

def logout_page(request):
    logout(request)
    return redirect('home')

#=====================================================================================

#====================================template=========================================
def home(request):
    contex = {}

    return render(request, 'index.html', contex)

def pengajuan(request):
    if request.method == 'POST':
        proposal = ketProposalForm(request.POST, request.FILES)
        if proposal.is_valid():
            proposal.save()
            messages.success(request, "Proposal Telah Di Ajukan, Silahkan Tunggu Email Balasannya")
            return redirect('home')
    else:
        proposal = ketProposalForm()
        messages.success(request, "Proposal tidak terkirim")
        

    contex={
        'proposal':proposal,
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