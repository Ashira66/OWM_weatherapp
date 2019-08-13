from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import weatherdata
#from django.http import HttpResponse
import urllib.request
import json

def index(request):
    wdata=[]
    #return HttpResponse("Hello,ATR!.")
    #persons = Person.objects.all().order_by('first_name')
    for loc in weatherdata.objects.all():
        #s='%s %s %s %s %s'%(w['name'],w['coord']['lat'],w['coord']['long'],w['weather'][0]['main'],w['weather'][0]['description'])
        #wdata.append(s)
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

    #return render(request, 'weatherapp/index.html', {'persons': persons})
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

#def contact_new(request):
#    if request.method == 'POST':
#        form = PersonForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('/')
#    else:
#        form = PersonForm()
#    return render(request, 'contact/contact_edit.html', {'form': form})
