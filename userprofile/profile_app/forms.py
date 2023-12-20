from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError("This password is too short. It must contain at least 8 characters.")
        if password1.isdigit():
            raise ValidationError("Password cannot be entirely numeric.")
        return password1

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
