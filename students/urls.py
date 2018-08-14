# users/urls.py
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('create/', views.GroupCreate.as_view(), name='create'),
]