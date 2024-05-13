# uppertester.py
import paho.mqtt.client as mqtt
import json
import time
import sys
import maintest  # Importez le module maintest pour accéder aux variables

# Configuration MQTT
broker_address = "194.57.103.203"
broker_port = 1883
topic_UT = "UT"
topic_RESP = "RESP"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic_UT)

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    if msg.topic == topic_UT:
        handle_upper_tester_message(msg.payload.decode())

def handle_upper_tester_message(payload):
    request = json.loads(payload)
    if request["command"] == "get_time":
        response = {"status": "success", "message": "Time sent successfully", "data": {"time": time.time()}}
    elif request["command"] == "get_pos":
        response = {"status": "success", "message": "Position sent successfully", "data": {"position": {"x": maintest.x, "y": maintest.y}}}
    else:
        response = {"status": "error", "message": "Unknown command"}
    response_json = json.dumps(response)
    client.publish(topic_RESP, response_json)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port, 60)
client.loop_start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
    client.loop_stop()
    client.disconnect()
