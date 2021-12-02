# Generated by Django 3.2.7 on 2021-12-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ketProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField(null=True)),
                ('jurusan', models.CharField(choices=[('Teknik Elektro', 'Teknik Elektro'), ('Teknik Informatika', 'Teknik Informatika'), ('Teknik Industri', 'Teknik Industri'), ('Sistem Informasi', 'Sistem Informasi'), ('Matematika', 'Matematika')], default='Teknik Elektro', max_length=20)),
                ('semester', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14)], default=1)),
                ('asal_instansi', models.CharField(default='', max_length=50, null=True)),
                ('noHP', models.IntegerField(null=True)),
                ('judul', models.CharField(max_length=50)),
                ('tujuan', models.TextField(max_length=1000)),
                ('tanggal_pelaksanaan', models.DateField(blank=True, null=True)),
                ('waktu_pelaksanaan', models.CharField(default='', max_length=50)),
                ('lokasi_pelaksanaan', models.CharField(default='', max_length=50)),
                ('rab', models.FileField(blank=True, upload_to='')),
                ('file_proposal', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
