from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, UserProfileForm

def index(request):
    return render(request, 'home/index.html')


class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "home/register.html"
    success_url = reverse_lazy('home:login')

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'home/profile.html'
    success_url = reverse_lazy('home:index')
    
    def get_object(self):
        return self.request.user