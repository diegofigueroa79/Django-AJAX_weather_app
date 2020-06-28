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
			if response['cod'] == 200:
				if not City.objects.filter(name=name).exists():	
					City(name=name).save()
				else:
					print("city already exists in db")
			
	
	form = CityForm()
	
	city_list = []
	for city in cities:
		response = r.get(url.format(city.name)).json()
		temp = ((response['main']['temp']) - 273.15) * (9/5) + 32
		city_info = {
			'name': response['name'],
			'country': response['sys']['country'],
			'temp': round(temp),
			'description': response['weather'][0]['description'],
			'icon': response['weather'][0]['icon'],			
		}
		city_list.append(city_info)
	
	context = {
		'city_list': city_list,
		'form': form,
	}
	
	return render(request, 'weather/weather.html', context)