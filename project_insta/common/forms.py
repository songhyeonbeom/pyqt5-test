from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    address = forms.CharField(label="주소")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2", "email", "address")

