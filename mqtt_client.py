import paho.mqtt.client as mqtt
import json


class mqtt_client:
    def __init__(self, address, port, clientID) -> None:

        self.mqttBroker = address
        self.port = port
        self.clientID = clientID
        self.client = None

    def connect_client(self):
        MQTT_KEEPALIVE_INTERVAL = 45
        self.client = mqtt.Client(self.clientID)
        self.client.connect(host="10.100.2.2", port=1883,
                            keepalive=MQTT_KEEPALIVE_INTERVAL)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.publish_to_topic(
                "homeassistant/sensor/front_cam_detection/state", "{'online': 'true'}")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected from MQTT server")
        self.client.loop.stop()

    def connect_client_secure(self, username, password):
        MQTT_KEEPALIVE_INTERVAL = 60
        self.client = mqtt.Client(self.clientID)
        self.client.connect(host=self.mqttBroker, port=self.port,
                            keepalive=MQTT_KEEPALIVE_INTERVAL)
        self.client = mqtt.Client(self.clientID)
        self.client.connect(self.mqttBroker)
        self.client.tls_set()  # <--- even without arguments
        self.client.username_pw_set(username=username, password=password)

    def publish_to_topic(self, topic: str, data: dict):
        message = json.dumps(data)
        self.client.publish(topic, message)
        print("Data published " + str(data))

    def on_message(self, mqttc, obj, msg):
        print("received message" + " " + str(msg.payload))
        # if i remove this and the following line, everything works fine
        self.client.disconnect()
        # but i have to disconnect and stop the loop after they received a message
        self.client.loop_stop()

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)
