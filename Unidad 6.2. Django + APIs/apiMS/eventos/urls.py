from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  # /
  path('', views.home, name='home'),

  ## URLS de inicio de sesión
  path('signin', views.sign_in, name='signin'),
  path('signout', views.home, name='signout'),
  path('nuevo', views.home, name='nuevo'),
  path('callback', views.callback, name='callback')
]
