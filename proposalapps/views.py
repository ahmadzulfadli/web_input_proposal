from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.http import FileResponse, HttpResponse
from django.core.mail import send_mail
from input_proposal.settings import EMAIL_HOST_USER
from django.core.files.storage import FileSystemStorage
import os
from input_proposal import settings

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

'''
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
'''

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
        email = request.POST.get('email',None)
        if proposal.is_valid():
            upload_file = request.FILES['rab']
            fs = FileSystemStorage()
            fs.save(upload_file.name , upload_file)
            proposal.save()
            pesan = "Proposal anda telah terkirim, silahkan tunggu email selanjutnya untuk mengetahui perkembangan proposal anda. Terimakasih"
            send_mail('Terkirim(Pengajuan Proposal FST)',pesan,EMAIL_HOST_USER, [email],fail_silently=False,)
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
    contex={
    }

    return render(request, 'hasil_pengaju.html', contex)

#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=================================template wd3========================================
def wakilDekan(request):
    sema = ketProposal.objects.filter(asal_instansi=6, keterangan_wd3=1).count()
    dema = ketProposal.objects.filter(asal_instansi=7, keterangan_wd3=1).count()
    lainnya = ketProposal.objects.filter(asal_instansi=8, keterangan_wd3=1).count()

    te = ketProposal.objects.filter(asal_instansi=1, keterangan_kaprodi=2, keterangan_wd3=1)
    tif = ketProposal.objects.filter(asal_instansi=2, keterangan_kaprodi=2, keterangan_wd3=1)
    tin = ketProposal.objects.filter(asal_instansi=3, keterangan_kaprodi=2, keterangan_wd3=1)
    sif = ketProposal.objects.filter(asal_instansi=4, keterangan_kaprodi=2, keterangan_wd3=1)
    mt = ketProposal.objects.filter(asal_instansi=5, keterangan_kaprodi=2, keterangan_wd3=1)

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
        model = ketProposal.objects.filter(asal_instansi=1, keterangan_kaprodi=2)
    elif system == 'tif':
        model = ketProposal.objects.filter(asal_instansi=2, keterangan_kaprodi=2)
    elif system == 'tin':
        model = ketProposal.objects.filter(asal_instansi=3, keterangan_kaprodi=2)
    elif system == 'sif':
        model = ketProposal.objects.filter(asal_instansi=4, keterangan_kaprodi=2)
    elif system == 'mt':
        model = ketProposal.objects.filter(asal_instansi=5, keterangan_kaprodi=2)
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
        'jum':model.count(),
        'acc':model.filter(keterangan_wd3 = 2).count(),
    }

    return render(request, 'atasan/list_proposalwd3.html', contex)

def viewswd3(request, id):
    model = get_object_or_404(ketProposal, id=id)

    email = model.email
    system = request.POST.get('system', None)
    pesan = request.POST.get('pesan', None)

    if system == 'revisi':
        model.keterangan_wd3_id = 3
        model.save(update_fields=['keterangan_wd3'])
        send_mail('Revisi(Wakil Dekan III)', pesan,EMAIL_HOST_USER,[email],fail_silently=False,)
        return redirect('wakilDekan')
    elif system == 'diterima':
        model.keterangan_wd3_id = 2
        model.save(update_fields=['keterangan_wd3'])
        send_mail('Diterima(Wakil Dekan III)', pesan + '(Proposal sudah di ACC Wakil Dekan III Fakultas Sains dan Teknologi Universitas Islam Negri Sultan Syarif Kasim Riau, silahkan temui Wakil Dekan III untuk info lebih lanjut)',EMAIL_HOST_USER,[email],fail_silently=False,)
        return redirect('wakilDekan')

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
        'jum':model.count(),
        'acc':model.filter(keterangan_kaprodi = 2).count(),
    }

    return render(request, 'kaprodi/kaprodi.html', contex)

def viewskaprodi(request, id):
    model = ketProposal.objects.get(id=id)
    
    #menampilkan file pdf
    fsock = open(model.rab.path, 'rb')
    response = HttpResponse(fsock, content_type='application/pdf')

    #menukar status
    email = model.email
    system = request.POST.get('system', None)
    pesan = request.POST.get('pesan', None)
    if system == 'revisi':
        model.keterangan_kaprodi_id = 3
        model.save(update_fields=['keterangan_kaprodi'])
        send_mail('Revisi(Kaprodi)',pesan,EMAIL_HOST_USER, [email],fail_silently=False,)
        return redirect('kaprodi')
        
    elif system == 'diterima':
        model.keterangan_kaprodi_id = 2
        model.save(update_fields=['keterangan_kaprodi'])
        send_mail('Diterima(Kaprodi)',pesan + '(Proposal akan diserahkan ke Wakil Dekan III untuk pemeriksaan lebih lanjut)',EMAIL_HOST_USER, [email],fail_silently=False,)
        return redirect('kaprodi')


    contex = {
        'model': model,
        'response':response,
    }

    return render(request, 'kaprodi/viewskaprodi.html', contex)
#=====================================================================================
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#=====================================================================================
#=====================================================================================
#-------------------------------------------------------------------------------------