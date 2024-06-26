from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
        

class RegisterDocForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    license_no = forms.CharField(label='License Number', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    class Meta:
        model = User
        fields = ('license_no', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(RegisterDocForm, self).__init__(*args, **kwargs)
            self.fields['license_no'].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
        