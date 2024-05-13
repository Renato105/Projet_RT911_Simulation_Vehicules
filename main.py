import paho.mqtt.client as mqtt
import json
import time

# Configuration MQTT
broker_address = "194.57.103.203"
broker_port = 1883
topic_publish = "vehicle"
topic_lights = "lights"
topic_top = "top"
# Définition des informations pour le véhicule
vehicle_data = {"id": "105", "vtype": 1, "x": 20, "y": 30, "dir": 1, "speed": 5}

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the desired topic when connected
    client.subscribe(topic_publish)
    client.subscribe(topic_lights)
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

def publish_vehicle_data(client, topic, data):
    # Convert the dictionary to a JSON string
    vehicle_json = json.dumps(data)
    # Publish the JSON data to the specified topic
    client.publish(topic, vehicle_json)

# Create an MQTT client
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the loop to listen for messages
client.loop_start()

try:
    while True:
        # Publish vehicle data
        publish_vehicle_data(client, topic_publish, vehicle_data)
        # Wait for one second before publishing the next message
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
    # Stop the MQTT loop and disconnect
    client.loop_stop()
    client.disconnect()
