from django.urls import path
from .views import (inicio, buscar_pacientes,pacientes,buscar_recetas, about,
                    RecetaListView, RecetaCreateView, RecetaDeleteView, RecetaDetailView, RecetaUpdateView,
                    PacienteUpdateView, PacienteDeleteView, PacienteDetailView, PacienteCreateView)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/buscar', buscar_pacientes, name='buscar_pacientes'),
    path('recetas/buscar', buscar_recetas, name='buscar_recetas'),
    path('about', about, name='about'),

    # urls con vistas basadas en clase
    path('crear-receta/', RecetaCreateView.as_view(), name='crear-receta'),
    path('listar-recetas/', RecetaListView.as_view(), name='listar-recetas'),
    path('detalle-receta/<int:pk>', RecetaDetailView.as_view(), name='detalle-receta'),
    path('eliminar-receta/<int:pk>', RecetaDeleteView.as_view(), name='eliminar-receta'),
    path('editar-receta/<int:pk>', RecetaUpdateView.as_view(), name='editar-receta'),
    path('editar-paciente/<int:pk>', PacienteUpdateView.as_view(), name='editar-paciente'),
    path('eliminar-paciente/<int:pk>', PacienteDeleteView.as_view(), name='eliminar-paciente'),
    path('detalle-paciente/<int:pk>', PacienteDetailView.as_view(), name='detalle-paciente'),
    path('crear-paciente/', PacienteCreateView.as_view(), name='crear_paciente'),

]
