from django.db import models
from django.db.models.deletion import CASCADE


JURUSAN = (
    ('Teknik Elektro','Teknik Elektro'),
    ('Teknik Informatika','Teknik Informatika'),
    ('Teknik Industri','Teknik Industri'),
    ('Sistem Informasi','Sistem Informasi'),
    ('Matematika','Matematika'),
)


class dataUser(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField(null=True)
    jurusan = models.CharField(max_length=20, choices=JURUSAN, default='Teknik Elektro')
    semester = models.IntegerField(choices=[(x,x) for x in range(1,15)], default=1)
    asal_instansi = models.CharField(max_length=50, default="", null=True)
    noHP = models.IntegerField(null=True)

class ketProposal(models.Model):
    data_pengaju = models.ForeignKey(dataUser, on_delete=models.CASCADE, default="")
    judul = models.CharField(max_length=50)
    tujuan = models.CharField(max_length=100)
    tanggal_pelaksanaan = models.DateField(blank=True, null=True)
    waktu_pelaksanaan = models.CharField(max_length=50, default="")
    lokasi_pelaksanaan = models.CharField(max_length=50, default="")
    rab = models.FileField(blank=True)
    file_proposal = models.FileField(blank=True)

