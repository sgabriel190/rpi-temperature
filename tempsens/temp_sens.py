import Adafruit_DHT
import RPi.GPIO as GPIO

# Pin defining and board mode
GPIO.setmode(GPIO.BOARD)
sensor = Adafruit_DHT.DHT11
pin = 4
led = 13
GPIO.setup(led, GPIO.OUT)

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
