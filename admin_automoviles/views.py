from .models import Automovil
from .forms import AutomovilForm
from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.

def lista_automoviles(request):
    autos = Automovil.objects.all()
    return render(request, 'lista.html', {'autos': autos})

def crear_automovil(request):
    if request.method == 'POST':
        form = AutomovilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_automoviles')
    else:
        form = AutomovilForm()
    return render(request, 'crear.html', {'form': form})

def detalle_automovil(request, id):
    auto = get_object_or_404(Automovil, id=id)
    return render(request, 'detalle.html', {'auto': auto})

def editar_automovil(request, id):
    auto = get_object_or_404(Automovil, id=id)
    if request.method == 'POST':
        form = AutomovilForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('lista_automoviles')
    else:
        form = AutomovilForm(instance=auto)
    return render(request, 'editar.html', {'form': form})

def eliminar_automovil(request, id):
    auto = get_object_or_404(Automovil, id=id)
    if request.method == 'POST':
        auto.delete()
        return redirect('lista_automoviles')
    return render(request, 'eliminar.html', {'auto': auto})