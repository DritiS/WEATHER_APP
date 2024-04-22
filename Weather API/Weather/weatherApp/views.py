from django.shortcuts import render
import json
import urllib.request
from .models import weather

def  index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=5e4e348d224cf3c50891c305659e3bf3').read()
       

        list_of_data = json.loads(source)

        weather_data = weather()
        weather_data.city = city
        weather_data.country = str(list_of_data['sys']['country'])
        weather_data.coordinate = str(list_of_data['coord']['lon']) + '' + str(list_of_data['coord']['lat'])
        weather_data.temperature = str(list_of_data['main']['temp']) + 'K'
        weather_data.pressure = str(list_of_data['main']['pressure'])
        weather_data.humidity = str(list_of_data['main']['humidity'])
        weather_data.save()

        backend_data = weather.objects.all()

        data = {
            "backend_data":backend_data,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + '' + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']) + 'K',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
        }
        
        
        print(data)
    else:
        data = {}
    return render(request,"index.html",data)
