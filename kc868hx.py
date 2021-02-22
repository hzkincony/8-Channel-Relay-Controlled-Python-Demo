#!/usr/bin/env python3

'''
KC868-H8 8 channel ethernet relay module - python demo code
Copyright (c) 2021 Hangzhou Kincony Electronics Co., Ltd.
All rights reserved.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
'''

import socket
import time

# Set KC868-H8 ip address and port, and connect
host = '192.168.1.210'
port = 4196
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

# Initialisation
s.sendto('RELAY-SCAN_DEVICE-NOW'.encode(),(host, port))
time.sleep(2)
s.sendto('RELAY-TEST-NOW'.encode(),(host, port))
time.sleep(2)

# Turn first relay on
s.sendto('RELAY-SET-1,1,1'.encode(),(host, port))
time.sleep(2)

# Turn first relay off
s.sendto('RELAY-SET-1,1,0'.encode(),(host, port))
time.sleep(2)

# Disconnect
s.close()
