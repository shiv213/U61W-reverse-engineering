# SANROCK U61W Drone Notes
sending packet every ~50ms

Shenzhen_63:cc:a2 (84:ea:97:63:cc:a2) (RA)	802.11	68	802.11 Block Ack, Flags=........C

Ports 6000 and 40000
Host port 6000 is receiving video
Drone port 40000 is sending video
Host port 5010 is sending instructions
Drone port 40000 is receiving instructions

Controls:
---
Control section of packet seems to be starting with hex bytes 63 63 and ending with 99


6363 0a00 000b 0066 8080 8080 8080 801c 8c99 45e1 423d

63630a00000b0066808080808080801c8c9945e1423d


Bytes:
---
63 63 0a 00 00 0b 00 66 80 80 80 80 80 80 80 0c 8c 99
aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar

aa - start of message (63)
ab - start of message (63)
ac - ?
ad - ?
ae - ?
af - ?
ag - ?
ah - start of frame (66)
ai - right stick X (neutral = 80)
aj - right stick Y (neutral = 80)
ak - left stick Y (neutral = 80)
al - left stick X (2f-d0) (neutral = 80)
am - trim vertical bar (base = 80)
an - trim right bar (base = 80)
ao - trim left bar (base = 80)
ap - 0c = neutral, 1c = take off, 2c = land
aq - ? see below
ar - end of frame (99)


aq:
---
wildcard command? 
checksum maybe? (XOR of ) 
modes: speed, headless

Tilt:
Joysticks (byte aq):
8c - low speed
84 - high speed
8e - headless mode low speed
86 - headless mode high speed


Example frame:
---
17:11:50.635419 2412 MHz 11n -27dBm signal antenna 1 26.0 Mb/s MCS 3 20 MHz long GI IP (tos 0x0, ttl 64, id 50828, offset 0, flags [none], proto UDP (17), length 46) 
    192.168.0.2.5010 > 192.168.0.1.40000: [udp sum ok] UDP, length 18
        0x0000:  4500 002e c68c 0000 4011 32df c0a8 0002  E.......@.2.....
        0x0010:  c0a8 0001 1392 9c40 001a d297 6363 0a00  .......@....cc..
        0x0020:  000b 0066 8080 8080 8080 800c 8c99       ...f.......... 


Kali VM Notes:
---
xrandr --newmode "1920x1080"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode Virtual1 1920x1080
xrandr --output Virtual1 --mode 1920x1080

airmon-ng start wlan0
airodump-ng wlan0mon
airodump-ng --channel 1 --bssid 84:EA:97:63:CC:A2 wlan0mon
tcpdump -i wlan0mon udp 'port 5010' -Xvv


Hardware:
---
udirc-WiFi-63CCA2
BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC
84:EA:97:63:CC:A2  -16       30        0    0   1   26   OPN
Shenzhen Icomm Semiconductor Co., Ltd.


        0x0000:  4500 0027 7215 0000 4011 875d c0a8 0002  E..'r...@..]....                                                                                                                                                                 
        0x0010:  c0a8 0001 1392 9c40 0013 5699 6363 0a00  .......@..V.cc..                                                                                                                                                                 
        0x0020:  0004 00a0 0001 0af2 5f8c a7              ........_..                                                                                                                                                                      

        0x0000:  4500 0027 3d72 0000 4011 bc00 c0a8 0002  E..'=r..@.......                                                                                                                                                                 
        0x0010:  c0a8 0001 1392 9c40 0013 5699 6363 0a00  .......@..V.cc..                                                                                                                                                                 
        0x0020:  0004 00a0 0001 0aef 2816 cd              ........(..                                                                                                                                                                      

        0x0000:  4500 0027 f983 0000 4011 ffee c0a8 0002  E..'....@.......                                                                                                                                                                 
        0x0010:  c0a8 0001 1392 9c40 0013 5699 6363 0a00  .......@..V.cc..                                                                                                                                                                 
        0x0020:  0004 00a0 0001 0acd 499c fd              ........I..            



		0x0000:  4500 002e 5089 0000 4011 a8e2 c0a8 0002  E...P...@.......                                                                                                                                                                 
        0x0010:  c0a8 0001 1392 9c40 001a d297 6363 0a00  .......@....cc..                                                                                                                                                                 
        0x0020:  000b 0066 8080 8080 8080 800c 8c99 9e70  ...f...........p                                                                                                                                                                 
        0x0030:  3492                                     4.                                                                                                                                                                               

        0x0000:  4500 002e c61f 0000 4011 334c c0a8 0002  E.......@.3L....                                                                                                                                                                 
        0x0010:  c0a8 0001 1392 9c40 001a d297 6363 0a00  .......@....cc..                                                                                                                                                                 
        0x0020:  000b 0066 8080 8080 8080 800c 8c99 2886  ...f..........(.                                                                                                                                                                 
        0x0030:  f713                                     ..                                                                                                                                                                               

4500 002e feac 0000 4011 fabe c0a8 0002 c0a8 0001 1392 9c40 001a d297 6363 0a00 000b 0066 8080 8080 8080 800c 8c99 45e1 423d

4500002efeac00004011fabec0a80002c0a8000113929c40001ad29763630a00000b0066808080808080801c8c9945e1423d

