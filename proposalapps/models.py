from django.db import models
from django.db.models.deletion import CASCADE

class StatusKaprodi(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class StatusWd3(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Instansi(models.Model):
    instansi = models.CharField(max_length=20)

    def __str__(self):
        return self.instansi

class ketProposal(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=20)
    semester = models.CharField(max_length=50)
    asal_instansi = models.ForeignKey(Instansi, on_delete=models.CASCADE, related_name='instansi_asal')
    noHP = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    judul = models.CharField(max_length=50)
    tujuan = models.TextField(max_length=1200)
    tanggal_pelaksanaan = models.DateField(blank=True, null=True)
    waktu_pelaksanaan = models.CharField(max_length=50, default="")
    lokasi_pelaksanaan = models.CharField(max_length=50, default="")
    rab = models.FileField(blank=True)
    file_proposal = models.FileField(blank=True)
    keterangan_kaprodi = models.ForeignKey(StatusKaprodi, on_delete=models.CASCADE, related_name='kaprodi_status', default=1)
    keterangan_wd3 = models.ForeignKey(StatusWd3, on_delete=models.CASCADE, related_name='wd3_status', default=1)

    published1 = models.DateField(auto_now_add=True)
    updated1   = models.TimeField(auto_now=True)

class formatFile(models.Model):
    formRab = models.FileField(blank=True)
    formFile = models.FileField(blank=True)