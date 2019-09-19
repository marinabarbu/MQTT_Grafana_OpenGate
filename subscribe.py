import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connect with Code: ", str(rc))
    #Subscribe Topic:
    client.subscribe("Test/#")

nr = 0

def on_message(client, userdata, msg):
    if(float(str(msg.payload)) > 25):
        nr = nr + 1
    if(nr == 10):
        print("ALERT!!!")
    print(str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("farmer.cloudmqtt.com", 16697, 60)
client.username_pw_set("yssrliya", "8a6l_tOwTMX9")
client.loop_forever()
