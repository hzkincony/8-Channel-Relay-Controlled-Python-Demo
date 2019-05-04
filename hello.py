# KC868 Smart Home Demo For Python-- Code By KinCony
#!/usr/bin/python
# --*-- coding:utf-8 --*--
import socket  
import time
host = '192.168.1.210'  #KC868-H8's ip address
port = 4196             #KC868-H8's port
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #Ebable ipv4 tcp/ip protocol
s.connect((host,port))                                     #Connect with Server
#-------------------------------------------------------

s.sendto('RELAY-SCAN_DEVICE-NOW'.encode(),('192.168.1.210', 4196))  #Send Initialization Command-1
time.sleep(2)                                                       #Delay 2S
s.sendto('RELAY-TEST-NOW'.encode(),('192.168.1.210', 4196))         #Send Initialization Command-2
time.sleep(2)                                                       #Delay 2S
s.sendto('RELAY-SET-1,1,1'.encode(),('192.168.1.210', 4196))        #Turn First Light ON
time.sleep(2)                                                       #Delay 2S
s.sendto('RELAY-SET-1,1,0'.encode(),('192.168.1.210', 4196))        #Turn First Light OFF
time.sleep(2)                                                       #Delay 2S
s.close()                                                           #DisConnect Socket

