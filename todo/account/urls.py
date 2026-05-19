from django.urls import path
from account.views import *

urlpatterns = [
    path('signup',SignUpView.as_view(),name="signup"),
    path('signin',SignInView.as_view(),name="signin"),
    path('deleteuser/<int:id>',DeleterUserView.as_view(),name="deleteuser")
]