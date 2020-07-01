from django.urls import path

from . import views


app_name = 'weather'
urlpatterns = [
	path('', views.home, name="home"),
	path('delete/<city_name>/', views.delete, name="delete"),
] 
