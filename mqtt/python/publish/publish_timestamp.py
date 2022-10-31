# cloud.iiotmq.com

import paho.mqtt.client as paho
import time


broker = "publicmqttbroker.iiotmq.com"
port = 1883


client = paho.Client("client-id-publish-12345")
client.username_pw_set("publicmqttbroker", "publicmqttbroker")
client.connect(broker, port)

for i in range(10000):
    t = int(time.time())
    ret = client.publish("timestamp", "%s" % t)  # publish
    print(ret)
    time.sleep(1)
