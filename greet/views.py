from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse('hello world')

from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "greet/index.html"