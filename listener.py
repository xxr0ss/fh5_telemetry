import sys
from socket import socket, AF_INET, SOCK_DGRAM
from utils import FH5_API
from utils.DataHelper import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('localhost', 8000))
api = FH5_API()

try:
    print_high_water = 0
    last_print_size = 0
    while True:
        api.fh_data = s.recv(324)
        speed = api.fh_data.Speed
        engine_rpm = api.fh_data.CurrentEngineRpm
        gear = api.fh_data.Gear
        content = 'Speed: {:.1f} km/h    Engine: {:.0f} rpm    Gear: {}'.format(
            get_speed_kph(speed),
            engine_rpm,
            get_gear_name(gear))
        sys.stdout.write(' ' * print_high_water + '\b' * print_high_water)
        sys.stdout.write('\b' * last_print_size)
        last_print_size = sys.stdout.write(content)
        print_high_water = max(last_print_size, print_high_water)
except KeyboardInterrupt:
    print('\nBye~')
