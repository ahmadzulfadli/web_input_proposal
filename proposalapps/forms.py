from cProfile import label
from random import choice, choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *


class ketProposalForm(forms.ModelForm):
    class Meta:
        model = ketProposal
        fields=['nama','nim', 'jurusan', 'semester', 'asal_instansi', 'email', 'noHP',
                'email','judul','tujuan','tanggal_pelaksanaan','waktu_pelaksanaan','lokasi_pelaksanaan',
                'rab','file_proposal'
                ]


class instansiForm(forms.ModelForm):
    class Meta:
        model = Instansi
        fields = '__all__'

class semesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'

class jurusanForm(forms.ModelForm):
    class Meta:
        model = Jurusan
        fields = '__all__'

class UserLogin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
