from django.shortcuts import render

def home(request):
    contex = {}

    return render(request, 'index.html', contex)

def pengajuan(request):
    contex={}

    return render(request, 'input.html', contex)

def panduan(request):
    contex={}

    return render(request, 'panduan.html', contex)