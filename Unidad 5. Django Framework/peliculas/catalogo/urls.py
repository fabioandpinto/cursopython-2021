from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_movies.as_view(), name = 'lista'),
    path('nuevo/', views.create_movie.as_view(), name = 'crear')
]
