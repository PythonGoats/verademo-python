from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

# Deals with HTTP request/response
def say_hello(request):
    return HttpResponse('hello')

def register(request):
    return render(request, 'app/register.html', {})

def login(request):
    return render(request, 'app/login.html',{})

class LoginView(TemplateView):
    template_name = 'app/login.html'
    extra_context = {}
