from django.contrib import admin

# Register your models here.
from .models import Paciente

register_models=[Paciente]
admin.site.register(register_models)
