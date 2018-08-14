

# Register your models here.
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm,GroupCreationForm
from .models import StudentRegistration,GroupCreation

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = StudentRegistration
    list_display = ['username', 'full_name','address1','address2','email','mobile_number','gender','dpt','batch_number']



admin.site.register(StudentRegistration, CustomUserAdmin)

admin.site.register(GroupCreation)