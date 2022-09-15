from dataclasses import field
from importlib.resources import contents
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from techblog_app.models import Comment
# from techblog_app.models import Post
# from django.forms import ModelForm
from django_quill.fields import QuillField, QuillFormField


# class BaseForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(BaseForm, self).__init__(*args, **kwargs)
#         for bound_field in self:
#             if hasattr(bound_field, "field") and bound_field.field.required:
#                 bound_field.field.widget.attrs["required"] = "required"


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


class QuillFieldForm(forms.Form):
    title = forms.CharField()
    content = QuillFormField()


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'image']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'content']

        Widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
