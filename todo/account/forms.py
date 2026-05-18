from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["username","first_name", "last_name", "email", "password1", "password2"]

