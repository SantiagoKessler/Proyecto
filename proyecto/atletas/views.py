from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView, DetailView,UpdateView
from django.urls import reverse_lazy
from .forms import PaisForm
from .models import Pais

def index(request):
    return render(request, 'atletas/index.html')

class PaisList(LoginRequiredMixin, ListView):
    model = Pais
    context_object_name = 'paises'
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Pais.objects.filter(nombre__icontains=q)
        return queryset

class PaisCreate(LoginRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    success_url = reverse_lazy('atletas:pais_list')


class PaisDetail(LoginRequiredMixin, DetailView):
    model = Pais
    template_name = 'atletas/pais_detail.html' 
    context_object_name = 'pais'  

    

class PaisUpdate(LoginRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    success_url = reverse_lazy('atletas:pais_list')


class PaisDelete(LoginRequiredMixin, DeleteView):
    model = Pais
    success_url = reverse_lazy('atletas:pais_list')
