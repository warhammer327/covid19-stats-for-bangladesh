from django.shortcuts import render,get_object_or_404, redirect
from .models import Home
import requests
from bs4 import BeautifulSoup
import re
# Create your views here.


def home(request):
	sitename = 'COVID-19 Tracker'
	link = requests.get('https://disease.sh/v2/countries/BD')
	link = link.json()

	by_division = Home.objects.latest('date')

	url = 'https://iedcr.gov.bd/'
	response = requests.get(url)

	info= re.findall(r'<h3>(\d+)</h3>',response.text)

	x = info[0]
	infos= re.findall(r'<td>(\d+)</td>',response.text)
	y = infos[8]



	args = {'sitename':sitename,'data':link,'by_division':by_division,'x':x,'y':y}
	return render(request,'front/home.html',args)
