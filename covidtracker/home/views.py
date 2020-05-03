from django.shortcuts import render,get_object_or_404, redirect
from .models import Home
import requests
# Create your views here.


def home(request):
	sitename = 'COVID-19 Tracker'
	link = requests.get('https://disease.sh/v2/countries/BGD?yesterday=true&strict=false')
	link = link.json()

	last_updated = link['updated']

	#print(link)
	args = {'sitename':sitename,'data':link}
	return render(request,'front/home.html',args)
