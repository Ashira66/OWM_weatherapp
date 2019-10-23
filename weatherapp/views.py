from django.shortcuts import render, get_object_or_404, redirect
from .models import weatherdata
import urllib.request
import json

def index(request):
    wdata=[]
    for loc in weatherdata.objects.all():
        url="http://api.openweathermap.org/data/2.5/weather?q=%s&appid=f15a75da67b6064f162f448e000955f8"%(loc)
        r= urllib.request.urlopen(url)
        d = r.read()
        jsondata= d.decode('utf-8').replace("'",'"')
        w=json.loads(jsondata)
        i=[]
        i.append(w['name'])
        i.append(w['coord']['lat'])
        i.append(w['coord']['lon'])
        i.append(w['weather'][0]['main'])
        i.append(w['weather'][0]['description'])
        wdata.append(i)
        #Creating the weather data
    return render(request, 'weatherapp/index.html', {'wdata':wdata})

def location_new(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = LocationForm()
        return render(request, 'weatherapp/index.html', {'form':form})
