from django.contrib import admin
from .models import Persona
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        'id',
        'departament',
        'first_name',
        'last_name',
        'position',
        'full_name'
    )
    # funcion para armar el full name
    def full_name(self,obj):
        fullname = obj.first_name + ' ' + obj.last_name
        return fullname

    list_filter = ('departament', 'position')

admin.site.register(Persona, PersonaAdmin)
