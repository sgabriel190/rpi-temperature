# Temperature sensor with led warning project

## Description
This application runs on a Raspberry Pi Zero W and a breadboard. The sensor data is displayed on a website.

This project can be ported to other Raspberry Pi machines with more hardware resources if needed. 

Currently the project includes a __Django__ and __Flask__ version. The Flask version is lighter than Django and it also does not include the LED. 

Each implementation includes a README file to go through implementation details and setup how-to.

## Getting Started

### Prerequisites

Installing the project to a bare metal machine, in this case raspberry pi, requires some environment check.

First, you need to make sure the machine is updated. Run the following commands in the terminal to update the machine:
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

Check if you have python3 installed by running in command line:
```
$ python3 --version
```

If not found, install python 3 with the following command:
```
$ sudo apt-get install python3
```

### Setup the breadboard and I/O pins

![Raspberry pi setup](https://i.ibb.co/qJShbz9/Annotation-2020-05-21-114706.jpg)

The setup for this project is simple. As it is displayed above, the electronic parts you need for this are: 
- Raspberry Pi(any version) 
- one led
- one DHT11 module
- 2 resistors(1k and 10k ohm)
- 4 male/female wires 
- 4 male/male wires for breadboard connection.

## Web application description

For client-side, the layout is based on static files(css, images, and javascript) and a template html file.

The javascript used on the client-side contains 2 functions. One of those updates the time based on the local machine time. The second function uses jQuery to update the page DOM asynchronous with data from the server.

## Add the script to systemctl 

Since systemctl runs on every Raspbian OS, it can take care of starting the DHT project each time the OS encounters an event.

Follow these steps to get the dht service running through systemctl:

- Create an application folder. __E.g__: create a dht_app folder at root level with all application content

- Create a service file which declares the new systemctl service

This is suggested to be created next to the other systemctl services(`/etc/systemd/system/`):

```
[Unit]
# Add a description for the new service.
Description=<description_text>

[Service]
User=root
# Use the application folder created at the first step.
WorkingDirectory=</app/directory>
# The paths will be relative to the WorkingDirectory set previously.
ExecStart=python3 <path/to/script.py>
Restart=always

[Install]
WantedBy=multi-user.target
```

- Reload the systemctl daemon

```
$ sudo systemctl daemon-reload
```

- Enable the service. The service name should be the filename created in the systemctl services

```
$ sudo systemctl enable service-name.service
```

- Start the service.

```
$ sudo systemctl start service-name.service
```

## Acknowledged problems

- Using this build is resource demanding, it may be not optimal to be run on a Raspberry Pi Zero W as the response times can be high.

- Using the multiprocessing tool on a single threaded computer doesn't bring the best result.

- The sensor is a cheap version and even if it displays precision of one(one decimal digit), the measure isn't precise.
