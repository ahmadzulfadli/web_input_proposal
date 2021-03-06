# Generated by Django 3.2 on 2022-02-23 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formatFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formRab', models.FileField(blank=True, upload_to='file_tamplate')),
                ('formFile', models.FileField(blank=True, upload_to='file_tamplate')),
            ],
        ),
        migrations.CreateModel(
            name='Instansi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instansi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jurusan', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StatusKaprodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatusWd3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ketProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.CharField(max_length=50)),
                ('noHP', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('judul', models.CharField(max_length=50)),
                ('tujuan', models.CharField(max_length=1200)),
                ('tanggal_pelaksanaan', models.DateField(blank=True, null=True)),
                ('waktu_pelaksanaan', models.CharField(default='', max_length=50)),
                ('lokasi_pelaksanaan', models.CharField(default='', max_length=50)),
                ('rab', models.FileField(blank=True, upload_to='rab')),
                ('file_proposal', models.FileField(blank=True, upload_to='proposal')),
                ('published1', models.DateField(auto_now_add=True)),
                ('updated1', models.TimeField(auto_now=True)),
                ('asal_instansi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instansi_asal', to='proposalapps.instansi')),
                ('jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurusan_pengaju', to='proposalapps.jurusan')),
                ('keterangan_kaprodi', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='kaprodi_status', to='proposalapps.statuskaprodi')),
                ('keterangan_wd3', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wd3_status', to='proposalapps.statuswd3')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_pengaju', to='proposalapps.semester')),
            ],
        ),
    ]
