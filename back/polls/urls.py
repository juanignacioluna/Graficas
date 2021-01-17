from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
	path('crear/', views.crear),
	path('getGrafica/', views.getGrafica),
	path('verGraficas/', views.verGraficas),
	path('eliminar/', views.eliminar),
]