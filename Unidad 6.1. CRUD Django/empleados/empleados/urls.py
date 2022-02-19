from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URLS del proyecto
    path('admin/', admin.site.urls),

    # URLS de las aplicaciones
    path('', include(('persona.urls', 'persona'), namespace='persona')),
    path('', include(('departamento.urls', 'departamento'), namespace='departamento'))
]
