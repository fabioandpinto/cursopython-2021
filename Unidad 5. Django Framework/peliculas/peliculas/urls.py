from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('usuarios.urls')),
    path('catalogo/', include('catalogo.urls'), name = 'listado'),
    path('usuarios/', include('django.contrib.auth.urls')),
]

"""
^accounts/login/$ [name='login']
^accounts/logout/$ [name='logout']
^accounts/password_change/$ [name='password_change']
^accounts/password_change/done/$ [name='password_change_done']
^accounts/password_reset/$ [name='password_reset']
^accounts/password_reset/done/$ [name='password_reset_done']
^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^accounts/reset/done/$ [name='password_reset_complete']
"""