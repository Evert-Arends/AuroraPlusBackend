from __future__ import print_function
from collections import namedtuple
from AuroraPlusBack.models import Servers, ServerData


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
        print(client_name, client_key, client_cpu, client_network_received, client_network_sent)

        client_server_obj = Servers.objects.get(Server_Key=str(client_key))
        if not client_server_obj:
            return False

        client_data_obj = None

        try:
            client_data_obj = ServerData.objects.get(Server_Key=client_key)
        except client_data_obj.DoesNotExist:
            return False

        client_data_obj.CPU_Usage = client_cpu
        client_data_obj.NetworkLoad_Sent = client_network_sent
        client_data_obj.NetworkLoad_Received = client_network_received

        client_data_obj.save()

        return True


