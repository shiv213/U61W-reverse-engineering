import socket
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)


DRONE_IP = '192.168.0.1'
CONTROL_PORT = 40000

try:
    s.connect((DRONE_IP, CONTROL_PORT))
    print("connected")
except:
    print("error")

data = b'63630a00000400a000010a'
count = 6

for x in range(count):
    s.send(binascii.unhexlify(data))

data = b'63630a00000b0066808080808080800c8c99'

while 1:
    s.send(binascii.unhexlify(data))

# data = b'63630a00000b0066808080808080801c8c99'
#
# while 1:
#     s.send(binascii.unhexlify(data))
