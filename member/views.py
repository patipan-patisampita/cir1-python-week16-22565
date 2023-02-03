from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    template = loader.get_template('myfirst.html')
    #return HttpResponse("Hello Member")
    return HttpResponse(template.render())