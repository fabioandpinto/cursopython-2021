from django.contrib import admin
from .models import Movies

# Registrar nuestro modelo adaptado al admin
class peliculaAdmin(admin.ModelAdmin):
    list_display = (
        'idPeli',
        'nombre',
        'genero',
        'completo'
    )

    def completo(self, obj):
        completo = str(obj.idPeli) + '- ' + obj.nombre
        return completo

    list_filter = ('genero',)

    search_fields = (
        'nombre', 'genero'
    )

    list_per_page = 5


# Registro mis modelos
admin.site.register(Movies, peliculaAdmin)

