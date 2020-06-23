from django.shortcuts import render

from .models import City
from .forms import CityForm

# Create your views here.
def home(request):
	cities = City.objects.all()
	
	form = CityForm()
	
	context = {
		'cities': cities,
		'form': form,
	}
	
	return render(request, 'weather/weather.html', context)