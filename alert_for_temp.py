import paho.mqtt.client as mqtt
import time

topic = 'Test/#'
lista_valori = []
prag = 25
depasiri_maxime = 5


def on_connect(client, userdata, flags, rc):
    print("Connect with Code: ", str(rc))
    #Subscribe Topic:
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(str(msg.payload)[2:-1])
    lista_valori.append(float(str(msg.payload)[2:-1]))
    #print(lista_valori)
    nr_depasiri = 0
    for v in lista_valori:
        if v > prag:
            nr_depasiri += 1
    if nr_depasiri >= depasiri_maxime:
        print("ALERT!!!")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("farmer.cloudmqtt.com", 16697, 60)
client.username_pw_set("yssrliya", "8a6l_tOwTMX9")
client.loop_forever()
