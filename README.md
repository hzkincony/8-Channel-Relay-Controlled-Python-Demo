# Hangzhou Kincony Electronics KC868-H series ethernet relay module: sample code and protocol documentation

This repository contains useful protocol documentation, sample and production source code for users of [Hangzhou Kincony Electronics KC868-H series ethernet relay modules](https://www.kincony.com/product/relay-controller).

The KC868-H series ethernet relay modules are available for purchase in the [KinCony AliExpress store](https://kincony.aliexpress.com):
- [KC868-H8 ethernet relay module](https://www.aliexpress.com/item/555377986.html)
- [KC868-H32 ethernet relay module](https://www.aliexpress.com/item/555335460.html)
- ...and more!

More resources are available at:
- the [Kincony website](https://www.kincony.com)
- the [Kincony YouTube channel](https://www.youtube.com/c/KinCony)
- the [Kincony forum](https://www.kincony.com/forum/)

## Sample code

These code samples demonstrate software control of the Hangzhou Kincony Electronics KC868-H series relay module.

Most samples demonstrate control via the local area network. The same protocol can also be used via a serial connection to the module's RS232 port.

Code samples are available for:
- [C++ (C++Builder)](https://github.com/hzkincony/32-channel-relay-controller-board-remote-control-by-C-Builder-internet) and [alternative](https://github.com/hzkincony/net_relay_control)
- [pascal (Delphi)](https://github.com/hzkincony/IP-Network-8-Channel-Relay-Control-Board-Controlled-by-Delphi)
- [python](https://github.com/hzkincony/8-Channel-Network-Relay-Controlled-By-Python)
- [Visual Basic .NET](https://github.com/hzkincony/IP-Network-8-Channel-Relay-Control-Board-Controlled-by-VB.net-in-LAN)


## Plugins and production application source code
- [Domoticz plugin (python)](https://github.com/hzkincony/Domoticz-KinCony-KC868-Ethernet-WiFi-Relay-Module-Plugin)
- [ESP8266 based web server for control of KC868-H series devices](https://github.com/hzkincony/BUILD-ESP8266-WEB-SERVER-NODEMCU-FOR-KC868-RELAY-CONTROLLER/blob/master/ESP8266_Web_Server.ino)
- [ESP8266 based voice control of KC868-H series using Google Home](https://github.com/hzkincony/NodeMCU-ESP8266-32-8-Channel-WiFi-Network-Relay-Board-Voice-Controlled-by-Google-Home-Assistant) 
- [ESP8266 based voice control of KC868-H series using Amazon Alexa](https://github.com/hzkincony/NodeMCU-ESP8266-32-8-Channel-WiFi-Network-Relay-Board-Voice-Controlled-by-Amazon-Alexa-Echo)
- [Home Assistant integration: tcp server to mqtt protocol translator](https://github.com/hzkincony/ethernet-relay-control-board-TCP-Socket-to-MQTT-protocol-kit-for-home-assistant)
- [KinCony KBOX Smart Home Android app](https://github.com/hzkincony/KBOX-Smart-Home-Android-App-LAN-Not-Need-Internet) and [alternative]()
- [KinCony KBOX Smart Home iOS app](https://github.com/hzkincony/KBOX-Smart-Home-iOS-App-LAN-Not-Need-Internet)
- [KC868-Hx Smart Controller Debugger (TCP client mode) ](https://github.com/hzkincony/ethernet-relay-module-Debugger-TCP-Client)
- [KC868-Hx Smart Controller Debugger (TCP server mode) ](https://github.com/hzkincony/ethernet-relay-module-Debugger-TCP-Server)

## Protocol documentation

The KC868-H series ethernet relay module acts as a tcp server on your local area network, listening on port 4196 by default. You can find the ip address of your relay module in the dhcp client table of your router.

Any tcp client can initiate the following interactions with the device:
- connect
- check the relay module type
- initialise
- switch an individual relay on or off
- check the status of an invididual array
- check the status of an input trigger
- check the serial number of the device
- switch all relays on or off at once
- check the status of all relays at once


### Checking the device model
- request: ```RELAY-SCAN_DEVICE-NOW```
- response: ```RELAY-SCAN_DEVICE-CHANNEL_8/CHANNEL_32, OK/ERROR```

### Open the working mode of the device server
- request: ```RELAY-TEST-NOW```
- response: ```HOST-TEST-START```

### Initialise the device
- request: ```RELAY–SCAN_DEVICE–NOW```
- response: ```RELAY-TEST-NOW```

### Switching one relay ON or OFF:
- request: RELAY-SET-x (1 byte pack_num), x (1 byte relay serial number), x (1 byte action 0 / 1)
- response: RELAY-SET-x (1 byte pack_num), X (1 byte relay serial number), x (1 byte action 0 / 1), OK/ERROR

### Separately checking the current switch status of one relay (as below picture):
- request: RELAY-READ-x (1 byte pack_num), x (1 byte relay sequence number)
- response: RELAY-READ-x (1 byte pack_num), x (1 byte relay sequence number), x (1 byte status 0 / 1), OK/ERROR

### Checking triggering input status:
- request: RELAY-GET_INPUT-x (1 byte pack_num)
- response: RELAY-GET_INPUT-x (1 byte pack_num), x (1 byte state), OK/ERROR

### Checking the device's serial number:
- request: ```RELAY-HOST-NOW```
- response: HOST-CHKLIC-56a890e6888793c918f151b5 (return the serial number).

### Switching multiple relays ON or OFF at once:

KC868-H8:
- request: RELAY-SET_ALL-x (1 byte pack_num), D0
- response: RELAY-SET_ALL-x (1 byte pack_num), D0, OK/ERROR

KC868-H32:
- request: RELAY-SET_ALL-x (1 byte pack_num), D3, D2, D1, D0
- response: RELAY-SET_ALL-x (1 byte pack_num), D3,D2,D1,D0,OK/ERROR

### Read multiple relays current switch status at a time:
- request: RELAY-STATE-x (1 byte pack_num)
- response (KC868-H8): RELAY-STATE-x (1 byte pack_num), D0, OK/ERROR
- response (KC868-H32): RELAY-STATE-x (1 byte pack_num), D3, D2, D1, D0, OK/ERROR
