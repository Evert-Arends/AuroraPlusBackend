from __future__ import print_function
import base64

import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from collections import namedtuple
from bin import client
from settings import constants as cfg
from AuroraPlusBack.models import Servers, ServerData
import json

Client = client.Client()


# Create your views here.


def index(request):
    version = cfg.VERSION
    hostname = cfg.HOSTNAME

    ok = "Hello and welcome to the AuroraPlus API, I have some information for you: \r\n" \
         "Version: {0} \r\n" \
         "Hostname: {1} \r\n".format(version, hostname)

    return HttpResponse(ok, request)


def profile_page(request, username):
    print(username)

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


@csrf_exempt
def post(request):
    received_json_data = json.loads(request.body)
    if received_json_data:
        print(received_json_data)
        # server = Servers(Name=)

        print(received_json_data["ServerDetails"]["NetworkLoad"]["Sent"])

        return HttpResponse('Data inserted')
    else:
        return HttpResponse('No post param :D:D:D')


@csrf_exempt
def add_client(request):
    received_json_data = json.loads(request.body)
    if not received_json_data:
        return HttpResponse('404 - No json object found in body.')

    action = received_json_data["Server"]["Action"]["Register"]
    if not action:
        return HttpResponse('No action found in json body.', status=400)
    if action == 'True':
        print('Registering server.')
    # LOAD ALL THE JSON IN TO THE NAMEDTUPLE

    server_data = namedtuple('ServerData', 'Name Key CPU_Usage Network_Sent Network_Received Action')

    server_name = received_json_data["Server"]["ServerDetails"]["ServerName"]
    server_key = received_json_data["Server"]["ServerDetails"]["ServerKey"]
    cpu = received_json_data["Server"]["ServerDetails"]["CPU_Usage"]
    network_sent = received_json_data["Server"]["ServerDetails"]["NetworkLoad"]["Sent"]
    network_received = received_json_data["Server"]["ServerDetails"]["NetworkLoad"]["Received"]

    server = server_data(server_name, server_key, cpu, network_sent, network_received, action)

    print(server.Network_Received)

    return HttpResponse(server)


@csrf_exempt
def update_client(request):
    json_body = json.loads(request.body)
    if not json_body:
        return HttpResponse('No json object found in body.', status=400)

    server_data = namedtuple('ServerData', 'Name Key CPU_Usage Network_Sent Network_Received Action Request_Date_Time')

    server_name = json_body["Server"]["ServerDetails"]["ServerName"]
    server_key = json_body["Server"]["ServerDetails"]["ServerKey"]
    cpu = json_body["Server"]["ServerDetails"]["CPU_Usage"]
    network_sent = json_body["Server"]["ServerDetails"]["NetworkLoad"]["Sent"]
    network_received = json_body["Server"]["ServerDetails"]["NetworkLoad"]["Received"]
    request_date_time = json_body["RequestDetails"]["Time"]["RequestSent"]

    action = json_body["Server"]["Action"]["Register"]
    if not action:
        return HttpResponse('No action found in json body.', status=400)
    if action == 'True':
        return HttpResponse('You are at the wrong page, moron.', status=400)

    server = server_data(server_name, server_key, cpu, network_sent, network_received, action)
    ordered_dict = server._asdict()

    update = Client.update_client(ordered_dict)

    if update:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def save_data(request):
    json_body = json.loads(request.body)
    if not json_body:
        return HttpResponse('No json object found in body.', status=400)

    save_client = Client.save_client(json_blob=json_body)
    if save_client:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def client_details(request, client_key, time=0):
    print(client_key)
    server_obj = ''
    print(time)
    time = int(time)

    try:
        server_obj = Servers.objects.filter(ServerKey=client_key)
    except server_obj.DoesNotExist:
        return HttpResponse('Fail.')

    if not server_obj:
        return HttpResponse('Fail.')

    try:
        if time == 0:
            server_data_obj = ServerData.objects.filter(ServerKey=client_key).last()
        else:
            date_now = datetime.datetime.now()
            old_date = date_now - datetime.timedelta(seconds=time)
            test = 'old_date: {0}', 'date_now: {1}'.format(old_date, date_now)
            print(test)
            server_data_obj = ServerData.objects.filter(ServerKey=client_key, RequestDate__range=(old_date, date_now))
    except ServerData.DoesNotExist:
        return False
    items = []
    if server_data_obj and time != 0:
        for item in server_data_obj:
            items.append(item.JsonData)

        json_blob = json.dumps(items)
        return HttpResponse(json_blob)

    if server_data_obj:
        item = server_data_obj.JsonData
        json_blob = json.dumps(item)

        return HttpResponse(json_blob)
    return HttpResponse(status=400)


