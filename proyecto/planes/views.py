from django.shortcuts import render, redirect, get_object_or_404
from atletas.models import Pais
from planes.models import Plan 
from .forms import PlanForm 

def index(request):
    return render(request, 'planes/index.html')

def asignar_plan(request, atleta_id):
    atleta = get_object_or_404(Pais, id=atleta_id)
    
    if atleta.velocidad == '5.4 segundos o más':  
        plan = "Plan exigente de mejora en velocidad"
    elif atleta.velocidad == '5.0 - 5.3 segundos':
        plan= "Plan de mejora de velocidad"
    else:
        plan = "Plan de mantenimiento"

    context = {
        'atleta': atleta,
        'plan': plan,
    }

    return render(request, 'planes/asignar_plan.html', context)

def index_planes(request):
    planes = Plan.objects.all()  
    return render(request, 'planes/index.html', {'planes': planes})

def plan_list(request):
   
    planes = Plan.objects.all()
    return render(request, 'planes/plan_list.html', {'planes': planes})

def plan_create(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planes:plan_list') 

    else:
        form = PlanForm()
    return render(request, 'planes/plan_create.html', {'form': form})

def plan_detail(request, id):
    plan = get_object_or_404(Plan, id=id)
    return render(request, 'planes/plan_detail.html', {'plan': plan})

def plan_update(request, pk):
    plan = get_object_or_404(Plan, pk=pk)  

    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('planes:plan_list')  
    else:
        form = PlanForm(instance=plan)

    return render(request, 'planes/plan_update.html', {'form': form})

def plan_delete(request, id):
    plan = get_object_or_404(Plan, id=id)

    if request.method == 'POST':
        plan.delete()
        return redirect('planes:index')  

    return render(request, 'planes/plan_confirm_delete.html', {'plan': plan})