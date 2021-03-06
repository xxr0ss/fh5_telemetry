import sys
from socket import (socket, AF_INET, SOCK_DGRAM, SOL_SOCKET,
                    SO_BROADCAST, gethostname, gethostbyname)
from threading import Thread, Event
from utils import FH5_Data, FH5_API


class Forward(Thread):
    def __init__(self):
        super().__init__()
        self.sock_src: socket = None
        self.sock_dst: socket = None
        self.dst_port = 0
        self._stop = False
        self._jsonify = True
        addr = gethostbyname(gethostname()).split('.')
        addr[-1] = '255'
        self.broadcast_addr = '.'.join(addr)

    def config(self, dst_port=50000, jsonify=True):
        self._jsonify = jsonify
        if self.sock_src:
            self.sock_dst.close()
        self.dst_port = dst_port

        sock_src = socket(AF_INET, SOCK_DGRAM)
        sock_src.bind(('localhost', 8000))
        self.sock_src = sock_src

        sock_dst = socket(AF_INET, SOCK_DGRAM)
        sock_dst.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.sock_dst = sock_dst

    def run(self):
        while not self._stop:
            raw_data = self.sock_src.recv(324)
            data = FH5_API(raw_data).to_json(
            ).encode() if self._jsonify else raw_data
            self.sock_dst.sendto(data, (self.broadcast_addr, self.dst_port))

    def stop(self):
        self._stop = True


if __name__ == '__main__':
    src_port = None

    forward = Forward()
    if '-d' in sys.argv:
        dst_port = int(sys.argv[sys.argv.index('-d')+1])
        forward.config(dst_port=dst_port)
    else:
        forward.config()

    forward.start()

    while True:
        if input().lower() in ('q', 'exit'):
            print('bye')
            forward.stop()
            break
