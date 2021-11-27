from django.db import models


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
    noHP = models.IntegerField(null=True)

class ketProposal(models.Model):
    judul = models.CharField(max_length=50)
    tujuan = models.CharField(max_length=100)

class rabProposal(models.Model):
    rab = models.FileField(blank=True)
