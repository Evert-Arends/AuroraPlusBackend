# Imports here.
import os

# Define server variables here.

API_SERVER_BASE = '127.0.0.1'
API_SERVER_PORT = '8001'
VERSION = 'V1.0'
HOSTNAME = os.uname()[1]


# Do not touch zone.
API_SERVER_ADDRESS = '{0}:{2}'.format(API_SERVER_BASE, ':', API_SERVER_PORT)


