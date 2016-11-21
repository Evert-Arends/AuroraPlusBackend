from __future__ import print_function
from collections import namedtuple
from AuroraPlusBack.models import Servers, ServerData
from django.core.exceptions import ObjectDoesNotExist


class Client:
    def __init__(self):
        pass

    def register_client(self):
        pass

    def update_client(self, server_dict):
        client_name = server_dict["Name"]
        client_key = server_dict["Key"]
        client_cpu = server_dict["CPU_Usage"]
        client_network_sent = server_dict["Network_Sent"]
        client_network_received = server_dict["Network_Received"]
        client_request_date_time = server_dict["Request_Date_Time"]
        print(client_name, client_key, client_cpu, client_network_received, client_network_sent)

        client_server_obj = Servers.objects.get(ServerKey=str(client_key))
        if not client_server_obj:
            return False

        client_data_obj = None

        try:
            client_data_obj = ServerData.objects.get(ServerKey=client_key)
        except client_data_obj.DoesNotExist:
            return False

        client_data_obj.CPU_Usage = client_cpu
        client_data_obj.NetworkLoad_Sent = client_network_sent
        client_data_obj.NetworkLoad_Received = client_network_received
        client_data_obj.RequestDate = client_request_date_time

        client_data_obj.save()

        return True

    def save_client(self, json_blob):
        json_blob = json.loads(json_blob)
        if not json_blob:
            print('No json blob found.')
            return

        json_blob = json.loads(json_blob)
        server_key = json_blob["Server"]["ServerDetails"]["ServerKey"]
        request_date = json_blob["RequestDetails"]["Time"]["RequestSent"]
        if not server_key:
            print('No ServerKey specified.')
            return

        try:
            client_details_obj = Servers.objects.get(ServerKey=server_key)
        except ObjectDoesNotExist:
            print('No object found.')
            return

        client_id = client_details_obj.Name

        if not client_id:
            print('No client with this name.')
            return

        new_entry = ServerData(JsonData=json_blob, ServerKey=server_key, RequestDate=request_date)
        json_blob = json.dumps(json_blob)
        new_entry = ServerData(JsonData=json_blob, ServerKey=server_key, RequestDate=datetime.datetime.now())
        new_entry.save()

        print('New entry for: {0}'.format(client_details_obj.Name))
        return True

