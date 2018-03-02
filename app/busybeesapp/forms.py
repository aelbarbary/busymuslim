from django import forms
from django.forms import ModelForm, SelectDateWidget, EmailInput,NumberInput,Select, Textarea, FileInput
from .models import *
import datetime
from registration.forms import RegistrationForm
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget

# class NewProfileForm(forms.ModelForm):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
#     class Meta:
#         model = Profile
#         exclude=['permission', 'last_login', 'is_staff', 'is_superuser']
#         label={
#             'phone': 'Phone'
#         }
