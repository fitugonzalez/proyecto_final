from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView

from .models import Paciente,Receta
from .forms import PacienteForm,RecetaForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'mi_primer_app/crear_paciente.html'
    success_url = reverse_lazy('pacientes')

@login_required
def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'mi_primer_app/pacientes.html', {'pacientes': pacientes})

def about(request):
    return render(request, 'mi_primer_app/about.html')

def buscar_pacientes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        pacientes = Paciente.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/pacientes.html', {'pacientes': pacientes, 'nombre': nombre})
    else:
        return redirect('inicio')  # Redirigir a inicio si no es una solicitud GET 
def buscar_recetas(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        recetas = Receta.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/listar_recetas.html', {'recetas': recetas, 'nombre': nombre})
    else:
        return redirect('inicio')  # Redirigir a inicio si no es una solicitud GET 
    
    
class RecetaListView(ListView):
    
    model = Receta
    template_name = 'mi_primer_app/listar_recetas.html'
    context_object_name = 'recetas'

class RecetaCreateView(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'mi_primer_app/crear_receta.html'
    success_url = reverse_lazy('listar-recetas')

class RecetaUpdateView(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'mi_primer_app/crear_receta.html'
    success_url = reverse_lazy('listar-recetas')

class RecetaDeleteView(DeleteView):
    model = Receta
    template_name = 'mi_primer_app/eliminar_receta.html'
    success_url = reverse_lazy('listar-recetas')

class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'mi_primer_app/detalle_receta.html'
    context_object_name = 'receta'

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'mi_primer_app/crear_paciente.html'
    success_url = reverse_lazy('pacientes')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'mi_primer_app/eliminar_paciente.html'
    success_url = reverse_lazy('pacientes')

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'mi_primer_app/detalle_paciente.html'
    context_object_name = 'paciente'

