import Adafruit_DHT
import RPi.GPIO as GPIO
import time
#from bs4 import BeautifulSoup
import os

# Pin defining and board mode
GPIO.setmode(GPIO.BOARD)
sensor = Adafruit_DHT.DHT11
pin = 4
led = 13
GPIO.setup(led, GPIO.OUT)

# Navigating os functions
def cdToRoot():
    try:
        os.chdir("/")
    except:
        print("Log: Error changing current directory to root.")

def cdToPath(path):
    try:
        cdToRoot()
        os.chdir(path)
    except:
        print("Log: Error changing currect directory to a specific path.")

# Defining functions
def printToFile(humidity, temperature):
    cdToPath("home/pi/temp")
    try:
        f = open("log.txt", "a")
        text = " temperature:" + str(temperature) + "\thumidity:" + str(humidity) +  " \ttime:" + str(time.strftime("%H:%M:%S",time.localtime())) + "\n"
        f.write(text) 
        f.close()
    except:
        print("Log: Error opening local log file.")

# Formatted print for terminal
def myPrint(humidity, temperature):
    print("temperature:",temperature,"humidity:",humidity,"time:",time.strftime("%H:%M:%S",time.localtime()))
    
# Formatted print for html website
def htmlPrint(humidity, temparature):
    cdToPath("var/www/html")
    try:
        html_file = open("temp.html", "w")
        html_content= "<h1>Local temperature</h1><p>temperature: %s humidity: %s time: %s</p>" % (temperature, humidity, time.strftime("%H:%M:%S",time.localtime()))
        html_file.write(html_content)
        html_file.close()
    except:
        print("Log: Error writing in the html file.")

# This function checks the threshold temperature and lights up an led
def checkTemperature(temperature, humidity, led):
    if(temperature < 21):
        GPIO.output(led, 0)
        printToFile(humidity, temperature)
    else:
        GPIO.output(led, 1)


# Get the first measures
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
myPrint(humidity, temperature)

# Main loop
while 1:
    time.sleep(2)
    try:
        new_humidity, new_temperature =  Adafruit_DHT.read_retry(sensor, pin)
        if(new_humidity != humidity or new_temperature != temperature):
            myPrint(new_humidity, new_temperature)
            htmlPrint(new_humidity, new_temperature)
        humidity = new_humidity
        temperature = new_temperature
        checkTemperature(temperature, humidity, led)
    except:
        print("Eroare la citire.")
