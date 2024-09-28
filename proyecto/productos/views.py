from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ProductoCategoria
from .forms import ProductoCategoriaForm

def index(request):
    return render(request, 'productos/index.html')

class ProductoCategoriaList(ListView):
    model = ProductoCategoria
    context_object_name = 'productocategorias' #De forma predeterminada es 'object_list'
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = ProductoCategoria.objects.filter(nombre__icontains=q)
        return queryset
    

class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy('productos:productocategoria_list')


class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria
  

class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("productos:productocategoria_list")


class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy('productos:productocategoria_list')