from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from account.forms import *
# Create your views here.

class TodoHomeView(View):
    def get(req,self):
        return render(req,"index.html")
    
class SignUpView(View):
    def get(self,req):
        # form = UserCreationForm()
        form = UserForm()
        return render(req,"signup.html",{"form":form})