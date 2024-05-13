import paho.mqtt.client as mqtt
import json
import time

# Configuration MQTT
broker_address = "127.0.0.1"
broker_port = 1883
topic_UT = "UT"
topic_RESP = "RESP"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the desired topics when connected
    client.subscribe(topic_UT)

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    if msg.topic == topic_UT:
        # Handle the message from the uppertester
        handle_upper_tester_message(msg.payload.decode())

def handle_upper_tester_message(payload):
    # Parse the JSON payload
    request = json.loads(payload)
    # Add your logic here to handle the request
    #...
    # Create a response
    response = {"status": "success", "message": "Request handled successfully"}
    # Convert the response to a JSON string
    response_json = json.dumps(response)
    # Publish the response to the topic_RESP topic
    client.publish(topic_RESP, response_json)

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
        # Wait for one second before checking for new messages
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
    # Stop the MQTT loop and disconnect
    client.loop_stop()
    client.disconnect()