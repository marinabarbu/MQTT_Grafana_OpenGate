
import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("log: " + buf)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)
def on_disconnect(client, userdata, flags, rc=0):
    print("DisConnected result code: " + str(rc))
def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8", "ignore"))
    print("message received", m_decode)

broker = "test.mosquitto.org"

client = mqtt.Client("python1")

client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_log = on_log
client.on_message = on_message
print("Connecting to broker ", broker)

client.connect(broker)
client.loop_start()
client.subscribe("house/sensor1")
client.publish("house/sensor1", "my first message")
time.sleep(4)
client.loop_stop()
client.disconnect()