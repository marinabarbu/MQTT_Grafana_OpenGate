import paho.mqtt.client as mqtt

#topic = 'meshliumfa30/WINSHI/#'
#topic = 'odsi/raspberry/marina_barbu'
topic = 'meshliumfa30/GAS_WiFi/#'

def on_connect(client, userdata, flags, rc):
    print("Connect with Code: ", str(rc))
    #Subscribe Topic:
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.beia-telemetrie.ro", 1883, 60)
client.loop_forever()
