from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['first_name','username','password1','password2','email']

    def __str__(self):
        return f"{self.name} {self.username} {self.email}"
