from dataclasses import field
from importlib.resources import contents
from pyexpat import model
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from library.models import Comment
# from django_quill.fields import QuillField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class CommentForm(forms.ModelForm):
    # content = forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Comment
        fields = ['title', 'content']
        # fields = ['title']

        Widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            # 'content': forms.Textarea(attrs={'class': 'wmd-input', 'id': 'wmd-input'}),
        }
