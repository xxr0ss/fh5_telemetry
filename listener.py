import sys
from socket import socket, AF_INET, SOCK_DGRAM

from utils.FH5 import FH5_API


def get_gear_name(gear):
    match gear:
        case 0:
            return 'R'
        case -1:
            return 'N'
        case _:
            return '%d' % gear

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
        content = 'Speed: %.1fkm/h    Engine: %.0f rpm    Gear: %s' % (speed * 3.6, engine_rpm, get_gear_name(gear))
        sys.stdout.write(' ' * print_high_water + '\b' * print_high_water)
        sys.stdout.write('\b' * last_print_size)
        last_print_size = sys.stdout.write(content)
        print_high_water = max(last_print_size, print_high_water)
except KeyboardInterrupt:
    print('\nBye~')