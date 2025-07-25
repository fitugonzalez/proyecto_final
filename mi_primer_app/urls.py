from django.urls import path
from .views import (inicio,
                    crear_paciente,buscar_pacientes,pacientes,buscar_recetas,
                    RecetaListView, RecetaCreateView, RecetaDeleteView, RecetaDetailView, RecetaUpdateView)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-paciente/', crear_paciente, name='crear_paciente'),
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/buscar', buscar_pacientes, name='buscar_pacientes'),
    path('recetas/buscar', buscar_recetas, name='buscar_recetas'),
    # urls con vistas basadas en clase
    path('crear-receta/', RecetaCreateView.as_view(), name='crear-receta'),
    path('listar-recetas/', RecetaListView.as_view(), name='listar-recetas'),
    path('detalle-receta/<int:pk>', RecetaDetailView.as_view(), name='detalle-receta'),
    path('eliminar-receta/<int:pk>', RecetaDeleteView.as_view(), name='eliminar-receta'),
    path('editar-receta/<int:pk>', RecetaUpdateView.as_view(), name='editar-receta'),

]
