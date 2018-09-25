import requests
import json
from .models import City
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CityForm


class HomePageView(TemplateView):
    template_name = "index.html"



def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={YOUR_API_KEY}'
    weather_data = []


    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:
        r = requests.get(url.format(city.name)).json()

        temp_C = round( (r['main']['temp'] - 32) * 5/9 , 2)

        city_data = {
            'city' : city.name,
            'temperature' : temp_C,
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_data)


    context = { 'weather_data': weather_data, 'form': form }
    return render(request, 'weather/weather.html', context)
