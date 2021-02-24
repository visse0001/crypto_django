from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from crypto.models import Producer, ProducerSymmetric



def index(request):
    producers_list = ProducerSymmetric.objects.all()
    template = loader.get_template('crypto/index.html')
    context = {
        'producers_list': producers_list,
    }
    return HttpResponse(template.render(context, request))