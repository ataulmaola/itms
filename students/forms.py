from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StudentRegistration,GroupCreation


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = StudentRegistration
        fields = ('username', 'full_name','address1','address2','email','mobile_number','gender','dpt','batch_number')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = StudentRegistration
        fields = ('username', 'full_name','address1','address2','email','mobile_number','gender','dpt','batch_number')

class GroupCreationForm(ModelForm):

    class Meta():
        model = GroupCreation
        fields = ["group_name","member_1" ,"member_2" ,"member_3"]

