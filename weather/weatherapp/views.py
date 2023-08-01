from django.shortcuts import render
import requests

def home(request):
    city=request.GET.get('city',"lucknow")
    #city="Lucknow"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=4daa1efb73fae7d1677708448568637f'
    data= requests.get(url).json()
    #print(data)
    payload={
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon' : data['weather'][0]['main'],
        'kelvin_temperature' :data['main']['temp'],
        'celcius_temperature' :int(data['main']['temp'] - 273),
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
    }
    
    context={'data':payload }
    #print(context)


    return render(request,'home.html',context)

# Create your views here