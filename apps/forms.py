from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from apps.models import *

class dataUserForm(forms.ModelForm):
    class Meta:
        model = dataUser
        fields = '__all__'

class ketProposalForm(forms.ModelForm):
    class Meta:
        model = ketProposal
        fields = '__all__'

class rabProposalForm(forms.ModelForm):
    class Meta:
        model = rabProposal
        fields = '__all__'