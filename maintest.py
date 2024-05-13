import paho.mqtt.client as mqtt
import json
import time

# Configuration MQTT
broker_address = "194.57.103.203"
broker_port = 1883
topic_publish = "vehicle"
topic_lights = "lights" 
#topic_top contient un message Go qui permet de donner le top depart pour tous les vehicules
topic_top = "top"
# topic_UT c'est le topic de l'envoi des requêtes de l'uppertester
topic_UT = "UT"
#topic_RESP c'est le topic de la réponse que l'on va faire par rapport  aux  requêtes de l'uppertester (On va publier nos réponses à l'uppertester sur ce topic)
topic_RESP= "RESP"


# Define x and y as global variables
x=20
y=30
#Définition des informations pour le véhicule
vehicle_data = {"id": "105", "vtype": 1, "x": x, "y": y, "dir": 1, "speed": 5}

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the desired topics when connected
    client.subscribe(topic_top)
    client.subscribe(topic_lights)
    client.subscribe(topic_UT)
    # client.subscribe(topic_lights) # Commenté pour l'instant

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    if msg.topic == topic_top:
        start_operations()
    # elif msg.topic == topic_lights: # Commenté pour l'instant
    #     handle_light_data(msg.payload.decode()) # Commenté pour l'instant

# def handle_light_data(payload): # Commenté pour l'instant
#     # Ajoutez une vérification pour détecter les guillemets simples et les remplacer par des guillemets doubles
#     payload = payload.replace("'", '"')
#     # Traiter les données des feux de signalisation
#     lights_data = json.loads(payload)
#     # Ajouter une logique pour réagir à l'état des feux (vert ou rouge)
#     if lights_data['state'] == 'green':
#         print("Feux verts. Le véhicule peut avancer.")
#         # Ajoutez ici la logique pour permettre au véhicule d'avancer
#     elif lights_data['state'] == 'red':
#         print("Feux rouges. Le véhicule doit s'arrêter.")
#         # Ajoutez ici la logique pour arrêter le véhicule ou attendre

def start_operations():
    # Commencez à publier les données de votre véhicule
    publish_vehicle_data(client, topic_publish, vehicle_data)
    # Commencez à écouter les données des autres véhicules
    client.subscribe(topic_publish)
    print("Vehicle operations started.")

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
