import logging
import time
import paho.mqtt.subscribe as subscribe

MQTT_server = "mqtt.beia-telemetrie.ro"
MQTT_port = 1883
logger = logging.getLogger(__name__)

#topic = 'meshliumfa30/WINSHI/#'
topic = 'odsi/raspberry/marina_barbu'

def on_message_print(client, userdata, message):
    print(str(message.payload))

def main():
    topic = 'odsi/raspberry/marina_barbu'
    while True:
        subscribe.callback(on_message_print,topic, hostname=MQTT_server, port=MQTT_port)
        time.sleep(5)

if __name__ == '__main__':
    main()