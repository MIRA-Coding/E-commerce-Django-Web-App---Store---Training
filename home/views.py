from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('LandPage.html')
    return render(request, 'LandPage.html')
# Create your views here.
