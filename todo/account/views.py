from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from account.forms import *
from django.contrib.auth import authenticate,login
# Create your views here.

class TodoHomeView(View):
    def get(req,self):
        form_data = User.objects.all()
        return render(req,"index.html",{"data":form_data})
    
class SignUpView(View):
    def get(self,req):
        # form = UserCreationForm()
        form = UserForm()
        return render(req,"signup.html",{"form":form})
    def post(self,req):
        form_data = UserForm(data=req.POST)
        
        if form_data.is_valid():
            form_data.save()
           
            messages.success(req,"SignUp Sucessfull ")
            return redirect('tdhome')
        messages.warning(req,"Error,Please Signup again !")
        return render(req,"signup.html",{"form":form_data})
    
class SignInView(View):
    def get(self,req):
        form = SigninForm()
        return render(req,"log.html",{"form":form})
    def post(self,req):
        form_data = SigninForm(data=req.POST)
        if form_data.is_valid():
            uname = form_data.cleaned_data.get('username')
            pswd = form_data.cleaned_data.get('password')

            user = authenticate(username=uname,password=pswd)
            if user:
                login(req,user)
                messages.success(req,"Sign In Sucessfull ")
                return redirect("tddash")
            else:
                messages.warning(req,"Invalid Username/Password ")
                return render(req,"signup.html",{"form":form_data})
    