from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template=loader.get_template('LandPage.html')
    return HttpResponse(template.render({},request))
    #home/templates/LandPage.html

# Create your views here.
