from scapy.all import rdpcap
from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep
from threading import Thread, Event


payloads = []

packets = rdpcap('horizon.pcap')


for pkt in packets:
    if pkt.payload.payload.name == 'UDP':
        payloads.append(pkt.payload.payload.load)


class Server(Thread):
    def __init__(self, port):
        super().__init__()
        self.port = port
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.__running = Event()
        self.__running.set()
        self.__active = Event()
        self.__active.set()

    def run(self):
        while self.__running.wait():
            for payload in payloads:
                self.__active.wait()
                if not self.__running.is_set():
                    return
                self.s.sendto(payload, ('localhost', 8000))
                sleep(0.035)
    
    def pause(self):
        self.__active.clear()
    
    def resume(self):
        self.__active.set()
    
    def stop(self):
        self.__active.set()
        self.__running.clear()
    
    def is_running(self):
        return self.__running.is_set()
    
    def is_active(self):
        return self.__active.is_set()


server = Server(8000)


def dispatch_cmd(cmd):
    match cmd:
        case 'pause':
            if not server.is_active():
                print('already paused')
            else:
                server.pause()
                print('paused')
        case 'resume' | 'continue':
            if server.is_active():
                print('already active')
            else:
                server.resume()
                print('resumed')
        case 'stop':
            server.stop()
            print('stoped')
        case 'status':
            print('active' if server.is_active() else 'paused')
        case 'exit' | 'q':
            server.stop()
            print('exiting...')
            exit(0)


if __name__ == '__main__':
    server.start()
    print('[*] fake server started')
    try:
        while True:
            cmd = input('> ')
            dispatch_cmd(cmd)

    except KeyboardInterrupt:
        server.stop()
        print('bye~')
        exit(0)