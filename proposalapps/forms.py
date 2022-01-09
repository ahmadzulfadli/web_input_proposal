from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *

class ketProposalForm(forms.ModelForm):
    class Meta:
        model = ketProposal
        #fields = '__all__'
        fields = ['nama', 'nim', 'jurusan', 'semester','asal_instansi','email','noHP','judul','tujuan','tanggal_pelaksanaan','waktu_pelaksanaan', 'lokasi_pelaksanaan', 'rab','file_proposal' ]

class instansiForm(forms.ModelForm):
    class Meta:
        model = Instansi
        fields = '__all__'

class UserLogin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
