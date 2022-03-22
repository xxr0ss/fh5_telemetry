from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 50000))
try:
    data = s.recv(324)
    print(data)
except KeyboardInterrupt:
    print('bye')
    s.close()