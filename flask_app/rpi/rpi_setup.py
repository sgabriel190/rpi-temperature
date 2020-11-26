from __future__ import absolute_import, unicode_literals
import Adafruit_DHT
import RPi.GPIO as GPIO

# Pin defining and board mode
GPIO.setmode(GPIO.BOARD)
sensor = Adafruit_DHT.DHT11
pin = 4
led = 13
GPIO.setup(led, GPIO.OUT)


# This function checks the threshold temperature and lights up an led
def checkTemperature(temperature: float):
    if temperature < 21:
        GPIO.output(led, 0)
    else:
        GPIO.output(led, 1)


# this method powers off the led
def powerOffLed():
    GPIO.output(led, 1)


# this method powers on the led
def powerOnLed():
    GPIO.output(led, 0)


# This method returns a dictionary for the html view with sensor values
def getInfo():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    checkTemperature(temperature)
    return dict(temperature=temperature, humidity=humidity)
