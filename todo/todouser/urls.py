from django.urls import path
from todouser.views import DashView
urlpatterns = [
    path('dash',DashView.as_view(),name="tddash"),
]