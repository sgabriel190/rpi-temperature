import os
import adafruit_dht
import board


sensor = adafruit_dht.DHT11(board.D4)

HOST=os.environ["DHT_IP"]
PORT=os.environ["DHT_PORT"]