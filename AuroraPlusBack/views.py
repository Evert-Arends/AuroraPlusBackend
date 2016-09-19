import base64

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Servers
import json


# Create your views here.
def index(request):
    t = request.get_full_path()
    ok = "hey {0} ".format(t)
    return HttpResponse(ok, request)


def profile_page(request, username):
    print username

    if Servers.objects.filter(Name=username):
        serverObj = Servers.objects.get(Name=username)
        servers = serverObj.Data
        try:
            servers = base64.b64decode(servers)
        except TypeError:
            servers = servers
    else:
        servers = 'No results found'
    return HttpResponse(servers)


def insert_page(request, name, data):
    if not Servers.objects.filter(Name=name):
        s = Servers(Name=name, Data=data)
        s.save()
        return HttpResponse('User created')
    else:
        return HttpResponse('User exists')


@csrf_exempt
def post_page(request, name):
    if Servers.objects.filter(Name=name):
        if request.POST.get('data'):
            data = request.POST.get('data')
            s = Servers.objects.get(Name=name)
            s.Data = data
            s.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('No use able POST request.')
    else:
        return HttpResponse('User does not exist')
