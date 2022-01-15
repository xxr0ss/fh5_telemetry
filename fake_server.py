from scapy.all import *
from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep


payloads = []

packets = rdpcap('horizon.pcap')


for pkt in packets:
    if pkt.payload.payload.name == 'UDP':
        payloads.append(pkt.payload.payload.load)


def run_server():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        while True:
            for payload in payloads:
                s.sendto(payload, ('localhost', 8000))
                print('sent')
                sleep(0.035)
    except KeyboardInterrupt:
        print('[server] bye~')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    run_server()