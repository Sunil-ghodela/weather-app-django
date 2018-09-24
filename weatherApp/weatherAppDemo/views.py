import requests
import json
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"



def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid='
    city = 'Delhi'

    r = requests.get(url.format(city)).json()

    weather_data = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    context = { 'weather_data': weather_data }

    return render(request, 'weather/weather.html', context)
