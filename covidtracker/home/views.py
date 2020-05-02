from django.shortcuts import render,get_object_or_404, redirect
from .models import Home
# Create your views here.


def home(request):
	sitename = 'COVID-19 Tracker'
	return render(request,'front/home.html',{'sitename':sitename})
