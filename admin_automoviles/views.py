from .models import Automovil
from .forms import AutomovilForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class AutomovilListView(LoginRequiredMixin, ListView):
    model = Automovil
    template_name = 'lista.html'
    context_object_name = 'autos'

class AutomovilDetailView(LoginRequiredMixin, DetailView):
    model = Automovil
    template_name = 'detalle.html'
    context_object_name = 'auto'

class AutomovilCreateView(LoginRequiredMixin, CreateView):
    model = Automovil
    form_class = AutomovilForm
    template_name = 'crear.html'
    success_url = reverse_lazy('lista_automoviles')

class AutomovilUpdateView(LoginRequiredMixin, UpdateView):
    model = Automovil
    form_class = AutomovilForm
    template_name = 'editar.html'
    success_url = reverse_lazy('lista_automoviles')

class AutomovilDeleteView(LoginRequiredMixin, DeleteView):
    model = Automovil
    template_name = 'eliminar.html'
    success_url = reverse_lazy('lista_automoviles')