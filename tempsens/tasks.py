from __future__ import absolute_import, unicode_literals
from celery import shared_task
"""
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Pin defining and board mode
GPIO.setmode(GPIO.BOARD)
sensor = Adafruit_DHT.DHT11
pin = 4
led = 13
GPIO.setup(led, GPIO.OUT)

# This function checks the threshold temperature and lights up an led
@shared_task
def checkTemperature(temperature, humidity, led):
    if(temperature < 21):
        GPIO.output(led, 0)
    else:
        GPIO.output(led, 1)

# this method powers off the led
@shared_task
def powerOffLed():
    GPIO.output(led, 1)

# This method returns a dictionary for the html view with sensor values
@shared_task
def getInfo():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    checkTemperature(temperature, humidity, led)
    return dict(temp = temperature, hum = humidity, time = str(time.strftime("%H:%M:%S",time.localtime())))
 """

 # Test method
 @shared_task
 def testTask():
     return "Test"