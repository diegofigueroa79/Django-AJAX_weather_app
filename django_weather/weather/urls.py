from django.urls import path

from . import views


app_name = 'weather'
urlpatterns = [
	path('', views.home, name="home"),
	path('add/', views.add, name="add"),
	path('delete/<city_name>/', views.delete, name="delete"),
] 
