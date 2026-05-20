from django import forms
from  todouser.models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ['user']
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"})
        }