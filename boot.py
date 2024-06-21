# boot.py -- run on boot-up
import network

wifiConfigFile = open('.env', 'r')
SSID = wifiConfigFile.readline()
SSI_PASSWORD = wifiConfigFile.readline()


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())


print("Connecting to your wifi...")
do_connect()

