from django.urls import path
from todouser.views import *
urlpatterns = [
    path('dash',DashView.as_view(),name="tddash"),
    path('addtodo',AddTodo.as_view(),name="addtodo"),
    path('deletetodo/<int:id>',DeleteTodoView.as_view(),name="deletetodo"),
    path('edittodo/<int:id>',EditTodoView.as_view(),name="edittodo"),
]