from django.shortcuts import render

import requests as r

from .models import City
from .forms import CityForm

# Create your views here.
def home(request):
	cities = City.objects.all()
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=ad066ae896d05c232621a2f18019a69b'
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name'].lower()
			response = r.get(url.format(name)).json()
			print(response['name'])
	
	form = CityForm()
	
	context = {
		'cities': cities,
		'form': form,
	}
	
	return render(request, 'weather/weather.html', context)