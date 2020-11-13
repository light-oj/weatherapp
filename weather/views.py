import requests
from django.shortcuts import render
from .models import City


# Create your views here.
def index(request):
    return render(request, 'weather/home.html', {})

def my_search(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=40984c59bd2c379848e2110dd7a1d2d3'
    city = request.POST.get('search')
    City.objects.create(name=city)
    r = requests.get(url.format(city)).json()
    if r['cod'] == '404':
        city_weather = {
            'city': city,
            'temperature': 'Not found',
            'description': 'Not found',
            "icon": '02d',
        }
    else:
        city_weather = {
                'city': r['name'],
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                "icon": r['weather'][0]['icon'],
            }
    context = {
        'city_weather': city_weather,
    }

    return render(request, 'weather/search.html', context)