import os
import sys
from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP, UDP
import socket
import binascii
import time
import sys
from pynput.keyboard import Key, Listener
from _thread import *

CALIBRATION = binascii.unhexlify(b'ff087e3f403fd0121200cb')  # ff08 7e3f 403f d012 1200 cb

DRONEIP = '192.168.0.1'
LOCALIP = 'localhost'
CONTROLPORT = 40000
VIDEOPORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

while 1:
    try:
        s.connect((DRONEIP, CONTROLPORT))
        print("connected")
        break
    except:
        continue


def keylistener(c):
    def on_press(key):
        global data
        inp = str(key)[1:2]
        data = b'ff087e3f403f9012120007'
        if inp == "q":  # arm
            data = b'ff087e3f403f90121240c7'
            return
        if inp == "e":  # up
            data = b'ff08fc3f403f9012120089'
            return
        if inp == "r":  # down
            data = b'ff08003f403f9012120085'
            return
        if inp == "w":  # forwards
            data = b'ff087e3f013f9012120046'
            return
        if inp == "s":  # backwards
            data = b'ff087e3f7f3f90121200c8'
            return
        if inp == "a":  # left
            data = b'ff087e3f40009012120046'
            return
        if inp == "d":  # right
            data = b'ff087e3f407e90121200c8'
            return
        if inp == "z":  # stop
            data = b'ff087e3f403f901212a069'
            return
        if inp == "y":  # disarm
            data = b'ff087e3f403f9012128087'
            return
        if inp == "1":  # left turn
            data = b'ff087e00403f9012120046'
            return
        if inp == "3":  # right turn
            data = b'ff087e7e403f90121200c8'

            return

    with Listener(on_press=on_press) as listener:
        listener.join()


def sendPackage():
    while 1:
        global data
        for n in range(0, 100):
            # print("Sending PACKAGE: " + data.decode())
            # print(binascii.unhexlify(data))
            s.send(binascii.unhexlify(data))
            # print("\n\n")
            time.sleep(0.03)
        data = b'ff087e3f403f9012120007'


# Send calibration first
for n in range(0, 100):
    print("Sending CALIBRATION...ff087e3f403fd0101000cb")
    s.send(CALIBRATION)
    time.sleep(0.05)

# start_new_thread(keylistener, ("",))
# start_new_thread(stream, ("",))
# start_new_thread(control, ("",))
sendPackage()

s.close()
