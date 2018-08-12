from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StudentRegistration

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = StudentRegistration
        fields = ('username', 'full_name','address1','address2','email','mobile_number','gender','dpt','batch_number')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = StudentRegistration
        fields = ('username', 'full_name','address1','address2','email','mobile_number','gender','dpt','batch_number')