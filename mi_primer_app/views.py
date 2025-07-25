from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView

from .models import Paciente,Receta
from .forms import PacienteForm,RecetaForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

@login_required   
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            nuevo_paciente = Paciente(
                nombre = form.cleaned_data['nombre'],
                apellido= form.cleaned_data['apellido'],
                edad= form.cleaned_data['edad'],
                fecha_nacimiento= form.cleaned_data['fecha_nacimiento'],
                enfermedad= form.cleaned_data['enfermedad'],
            )
            nuevo_paciente.save()
            return redirect('pacientes')
    else:
        form = PacienteForm()
        return render(request,"mi_primer_app/crear_paciente.html",{"form":form})
@login_required
def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'mi_primer_app/pacientes.html', {'pacientes': pacientes})


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
