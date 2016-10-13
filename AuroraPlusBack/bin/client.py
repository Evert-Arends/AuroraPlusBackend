from collections import namedtuple
from AuroraPlusBack.models import Servers


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
        print client_name, client_key, client_cpu, client_network_received, client_network_sent

        client_obj = Servers.objects.get(Server_Key=str(client_key))



