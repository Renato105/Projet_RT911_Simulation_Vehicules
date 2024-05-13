Simulation de véhicules avec MQTT


Ce projet consiste à simuler les mouvements de véhicules dans un espace restreint en utilisant MQTT pour la communication entre les différents composants du système.

Description du projet


L'objectif de ce projet est de simuler le mouvement de véhicules dans un espace restreint modélisé par une carte, où les véhicules peuvent se déplacer le long de voies dédiées et respecter les feux de signalisation aux intersections. Les véhicules envoient périodiquement leurs positions à un broker MQTT, qui distribue ensuite ces informations aux autres véhicules et aux parties intéressées du système.

Le projet est divisé en deux parties principales :

Code principal (maintest.py) : Ce fichier contient le code principal pour la simulation des véhicules. Il utilise MQTT pour publier les positions des véhicules et écouter les positions des autres véhicules ainsi que les informations sur les feux de signalisation.

UPPER_TESTER (uppertester.py) : Ce fichier contient le code pour un composant supplémentaire appelé UPPER_TESTER, qui permet de tester et de contrôler le système. L'UPPER_TESTER peut envoyer des requêtes pour obtenir le temps actuel ou la position d'un véhicule spécifique.

Installation et utilisation


Installation des dépendances :

Assurez-vous d'avoir Python installé sur votre système.
Installez les bibliothèques requises en exécutant pip install paho-mqtt.
Exécution du code :

Pour exécuter le code principal, utilisez la commande python maintest.py.
Pour exécuter l'UPPER_TESTER, utilisez la commande python uppertester.py.
Communication avec le système :

Utilisez l'UPPER_TESTER pour envoyer des requêtes spécifiques au système, telles que get_time() pour obtenir le temps actuel ou get_pos() pour obtenir la position d'un véhicule.


Structure du projet


maintest.py : Code principal pour la simulation des véhicules.


uppertester.py : Code pour l'UPPER_TESTER qui contrôle le système.


README.md : Ce fichier README décrivant le projet.
