from django.shortcuts import render,redirect
from django.views import View
from todouser.forms import *
from django.contrib import messages
from todouser.models import *

# Create your views here.

class DashView(View):
    def get(self,req):
        todolist = Todo.objects.filter(user= req.user)
        
        return render(req,'dash.html',{'todos':todolist})
    
class AddTodo(View):
    def get(self,req):
        form = TodoForm()
        # messages.success(req,"add todo")
        return render(req,"addtodo.html",{"form":form})
    def post(self,req):
        user = req.user
        form_data = TodoForm(req.POST)
        if form_data.is_valid():
            todo = form_data.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('tddash')
        return render(req,"addtodo.html",{"form":form_data})
    
class DeleteTodoView(View):
    def get(self,req,**kwargs):
        id = kwargs.get('id')
        Todo.objects.get(id=id).delete()
        messages.warning(req,"deleted")
        return redirect('tddash')

class EditTodoView(View):
    def get(self,req,**kwargs):
        id = kwargs.get('id')
        qso = Todo.objects.get(id= id)
        form = TodoForm(instance=qso)
        return render(req,"edittodo.html",{"form":form})
