import random
import sys
import time

from Adafruit_IO import MQTTClient
from simple_ai import *
from uart import *

AIO_FEED_IDs = ["nutnhan1", "nutnhan2", "ai"]
AIO_USERNAME = "huytran1305"
AIO_KEY = ""


def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong ...")


def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
    if feed_id == "nutnhan1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "nutnhan2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
# counter = 5
counter_ai = 5
while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 5
    #     temp = random.randint(10, 30)
    #     client.publish("cambien1", temp)
    #     light = random.randint(10, 100)
    #     client.publish("cambien2", light)
    #     humidity = random.randint(10, 100)
    #     client.publish("cambien3", humidity)

    counter_ai = counter_ai - 1

    if counter_ai <= 0:
        counter_ai = 5
        ai_result = image_dectector()
        # print("AI: ", ai_result)
        client.publish("ai", ai_result)

    readSerial(client)

    time.sleep(2)

    pass