from django.shortcuts import render,get_object_or_404
from django.http import Http404
# Create your views here.
# 
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm,GroupCreationForm
from .models import GroupCreation,StudentRegistration

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# def GroupCreate(request):
# 	form=GroupCreationForm()
# 	context={"form":form,}
# 	return render(request,"create.html",context)


# class GroupCreate(generic.CreateView):
#     form_class = GroupCreationForm
#     template_name = 'create.html'

class GroupCreate(LoginRequiredMixin,generic.CreateView):
    template_name = 'create.html'
    form_class = GroupCreationForm
    model = GroupCreation
    success_url = reverse_lazy('create')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Do any custom stuff here
        self.object.save()
        return super().form_valid(form)
