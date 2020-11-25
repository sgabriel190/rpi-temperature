# Temperature sensor with led warning project

## Description
This application runs on a Raspberry Pi Zero W and a breadboard. The sensor data is displayed on a website powered by Django and Celery.

This project can be ported to other Raspberry Pi machines with more hardware resources if needed. 

The django framework helps in creating a quick web server. As described by the developer himself, celery is a distributed task queue, which helps the server-side tasks to be asynchronous, while boosting its response time.

Each time the web client accesses the application, it updates the data and I find it useful to have control over the LED.

For client-side, the layout is based on static files(css, images, and javascript) and a template html file. Those files can be found and modified in `/templates/tempsens/` for templates and `/static/tempsens/` for static files.

The javascript used on the HTTP client contains 2 functions. One of those updates the time based on the local machine time. The second function uses jQuery to update the page DOM asynchronous with data from the server.

## Getting Started

### Setup the breadboard and I/O pins

![Raspberry pi setup](https://i.ibb.co/qJShbz9/Annotation-2020-05-21-114706.jpg)

The setup for this project is simple. As it is displayed above, the electronic parts you need for this are: 
- Raspberry Pi(any version) 
- one led
- one DHT11 module
- 2 resistors(1k and 10k ohm)
- 4 male/female wires 
- 4 male/male wires for breadboard connection.

### Installing

The language used in this project is python3. The raspberry pi machine requires Django and Celery installed.

First, you need to make sure the machine is updated. Run the following commands in the terminal to update the machine:
```
    $ sudo apt-get update
    $ sudo apt-get upgrade
```

Check if you have python3 installed by running in command line:
```
    $ python3
    >>>quit()
```

This command should run the python3 interpreter, if it exists, then the `quit()` method exits it.

If not found, install python 3 with the following command:
```
    $ sudo apt-get install python3
```

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

## Acknowledged problems

- Using this build is resource demanding, it may be not optimal to be run on a Raspberry Pi Zero W as the response times can be high.

- Using the multiprocessing tool on a single threaded computer doesn't bring the best result.

- The sensor is a cheap version and even if it displays precision of one(one decimal digit), the measure isn't precise.

## Resources and references

[Django documentation](https://towardsdatascience.com/image-panorama-stitching-with-opencv-2402bde6b46c)

[Celery documentation](https://docs.celeryproject.org/en/stable/)