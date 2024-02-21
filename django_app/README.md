# Django project

`THIS VERSION IS NO LONGER UPDATED.`

## Description

The django framework helps in creating a quick web server. As described by the developer himself, celery is a distributed task queue, which helps the server-side tasks to be asynchronous, while boosting its response time.

Each time the web client accesses the application, it updates the data and it useful to have control over the LED.

## Installing

The language used in this project is python3. The raspberry pi machine requires Django and Celery installed.

The temperature sensor requires a module for picking up the temperature in the environment.
```
$ sudo pip3 install Adafruit_DHT
```

With those installed, proceed to install django and celery:
```
$ sudo pip3 install django
$ sudo pip3 install celery
```

I recommend installing those with sudo privileges, because we need sudo for running the website on HTTP port 80. Rebooting the machine is an option here, but it is not usually necessary.

The celery framework needs a message broker: redis or rabbitMQ are one of those.

Installing redis:
```
$ sudo apt-get install redis
$ sudo pip3 install redis
```

### Running the application

After the packages are installed, the celery worker is ready to run. Enter the app folder and execute:
```
$ sudo celery -A temp_website worker -l info -n worker
```
It is possible to have more than one worker on the machine. Run the previous command with a different name for the “-n” argument. The workers will automatically synchronize. 

Run the django project from the app folder with:
```
$ sudo python3 manage.py runserver ip:80
```

The ip bit in the command should be the local IPv4 of the machine you are running this app on. If it is hard to find out your local network IPv4 run these commands:
```
$ python3
>>>import socket
>>>socket.gethostbyname_ex(socket.gethostname())[-1][-1]
```
Returns 127.0.0.1 on machines having the hostname in `/etc/hosts` as 127.0.0.1.

Browse to `/temp_website/settings.py` and add your IPv4 address to the `ALLOWED_HOSTS` list.

## Changing the temperature threshold

As some of you want to change the temperature threshold, it is possible. The value is hardcoded into one of the Celery tasks. Go to `/tempsens/tasks.py` and edit the following task:

```
# This function checks the threshold temperature and lights up an led
@shared_task
def checkTemperature(temperature, humidity, led):
	if(temperature < 21):
		GPIO.output(led, 0)
	else:
		GPIO.output(led, 1)
```

The function takes a decision based on the temperature and if it's below 21 then the led lights up. The led turns off otherwise.

## Change I/O pins settings

All the Raspberry Pi settings and functionalities are included into the `/tempsens/tasks.py` script.

```
import Adafruit_DHT
import RPi.GPIO as GPIO

# Pin defining and board mode
GPIO.setmode(GPIO.BOARD)
sensor = Adafruit_DHT.DHT11
pin = 4
led = 13
GPIO.setup(led, GPIO.OUT)
```

This code part sets up all the Raspberry Pi ports for the application.

## Resources and references

[Django documentation](https://towardsdatascience.com/image-panorama-stitching-with-opencv-2402bde6b46c)

[Celery documentation](https://docs.celeryproject.org/en/stable/)
