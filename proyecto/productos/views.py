from django.shortcuts import render, redirect
from .models import ProductoCategoria
from .forms import ProductoCategoriaForm

def index(request):
    return render(request, 'productos/index.html')

def productocategoria_list(request):
    query = request.GET.get('q')
    if query:
        productocategorias = ProductoCategoria.objects.filter(nombre__icontains=query)
    else:
        productocategorias = ProductoCategoria.objects.all()
    contexto = {'productocategorias' : productocategorias}
    return render(request,'productos/productocategoria_list.html', contexto)

def productocategoria_create(request):
    print(request.method)
    if request.method == 'GET':
        form = ProductoCategoriaForm()
       
    if request.method == "POST":
        form = ProductoCategoriaForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect("productos:productoscategoria_list")
    return render(request,'productos/productocategoria_create.html', {'form': form} )

