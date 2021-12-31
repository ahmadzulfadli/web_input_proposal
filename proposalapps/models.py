from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

class ketProposal(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=20)
    semester = models.CharField(max_length=50)
    asal_instansi = models.CharField(max_length=50, default="", null=True)
    noHP = models.CharField(max_length=50)
    judul = models.CharField(max_length=50)
    tujuan = models.TextField(max_length=1200)
    tanggal_pelaksanaan = models.DateField(blank=True, null=True)
    waktu_pelaksanaan = models.CharField(max_length=50, default="")
    lokasi_pelaksanaan = models.CharField(max_length=50, default="")
    rab = models.FileField(blank=True)
    file_proposal = models.FileField(blank=True)

    published = models.DateField(auto_now_add=True)
    updated   = models.TimeField(auto_now=True)

class formatFile(models.Model):
    formRab = models.FileField(blank=True)
    formFile = models.FileField(blank=True)
    