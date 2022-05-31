# from django.shortcuts import render



from django.http import HttpResponse
from django.template import loader

from .models import Bb

def index(request):
    # return HttpResponse("Здесь будет текст...")
    template=loader.get_template('firstApp/index.html')
    bbs=Bb.objects.order_by('-published')
    context= {'bbs': bbs}
    return HttpResponse(template.render(context,request))
