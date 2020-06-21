from django.shortcuts import render

from .models import City

# Create your views here.
def home(request):
	cities = City.objects.all()
	
	context = {
		'cities': cities,
	}
	
	return render(request, 'weather/weather.html', context)