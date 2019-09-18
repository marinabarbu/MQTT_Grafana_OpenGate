import json
import logging
import time
import paho.mqtt.publish as publish
import psutil

MQTT_server = "mqtt.beia-telemetrie.ro"
MQTT_port = 1883
logger = logging.getLogger(__name__)
#topic = 'meshliumfa30/WINSHI/#'
topic = 'odsi/raspberry/marina_barbu'
def main():

    while True:
        mem = psutil.virtual_memory()
        data = {'availableMemory':mem.available,
                'freeMemory':mem.free,
                'usedMemory':mem.used,
                }

        payload = json.dumps(data)
        print("Topic: {0}".format(topic))
        print("Payload: {0}".format(payload))
        publish.single(topic, payload=payload,
                       hostname=MQTT_server, port=MQTT_port)
        time.sleep(15)


if __name__ == '__main__':
    main()