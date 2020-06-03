from django.shortcuts import render,get_object_or_404, redirect
from .models import Home
import requests
from bs4 import BeautifulSoup
import re
# Create your views here.


def home(request):
	sitename = 'COVID-19 Tracker'

	by_division = Home.objects.latest('date')

	url = 'https://www.worldometers.info/coronavirus/'
	response = requests.get(url)

	#info= re.findall(r'>(\d+)</td>',response.text)
	full=response.text
	start=(full.find('bangladesh'))
	data=''
	for i in range(start,start+900):
		data += full[i]

	info = re.findall(r'>([^;]*)</td>',data)
	print(info[7])
	totalCases = info[1]
	newCases = info[2]
	totalDeaths = info[3]
	newDeaths = info[4]
	activeCases = info[7]
	testPerMil=info[9]


	args = {'sitename':sitename,'by_division':by_division,'totalCases':totalCases,'newCases':newCases,'totalDeaths':totalDeaths,'newDeaths':newDeaths,'activeCases':activeCases,'testPerMil':testPerMil}
	return render(request,'front/home.html',args)
