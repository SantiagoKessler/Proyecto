from django.shortcuts import render, redirect
from .forms import PaisForm
from .models import Pais

def index(request):
    return render(request, 'atletas/index.html')

def pais_list(request):
    query = request.GET.get('q')
    if query:
        paises = Pais.objects.filter(nombre__icontains=query)
    else:
        paises = Pais.objects.all()
    contexto = {'paises': paises}
    return render(request, 'atletas/pais_list.html', contexto)

def pais_create(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atletas:pais_list')
    else:
        form = PaisForm()
    return render(request, 'atletas/pais_create.html', {'form': form})
