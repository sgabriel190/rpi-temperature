# Flask project

## Description

The Flask implementation for this project, is a lightweight one which allows boards such as _Raspberry Pi 0w_ to run it.

This implementation does not include also the LED alert for thresholds.

The whole web application is served by Flask, static content and backend endpoints.

## Installing

The python packages required for this project to run are included in the `requirements.txt` file. To install them run `pip3 install -r requirements`. For Raspbian 12+, some additional apt packages are required: __python3-full__ and __python3-dev__.

__RECOMMENDATION__: Use a virtual environment for setting up python environment. This can be done with `python3 -m venv <environment_name>`. __REQUIRED__: Install the venv apt package: `sudo apt install python3-venv`

## Setting the environment variables

The Flask server uses environment variables in order to set the **IP:PORT** for the socket. Please set the DHT\_IP and DHT\_PORT variables before running the app.

Set the environment variables as such:
```
	export DHT_IP=x.x.x.x
	export DHT_PORT=xxxx
```

## Docker encapsulation

The Flask project can now use Docker to build and run a container. First installing Docker engine on your machine is **required**. Please follow any tutorial on the web to install it successfully.

The Docker image needs to be build and then ran with the following commands:
```
	cd to/flask/project/path
	docker build container-name:1.0.0 .
	docker run -d -p 80:80 --name=container-name --privileged -v /path/to/local/machine/logs/:/app/logger/ -e DHT_IP=0.0.0.0 -e DHT_PORT=80 container-name:1.0.0
```

Having those commands in mind you can name the image and container anything. Also the application uses environment variables to set the IP:HOST of the socket listening to requests.

The log file is stored on the local machine using __Docker volumes__.

## Resources and references

[Install Docker on Raspberry Pi](https://docs.docker.com/engine/install/raspberry-pi-os/)

[Create Docker containers](https://docs.docker.com/guides/walkthroughs/run-a-container/)

[Flask](https://flask.palletsprojects.com/en/3.0.x/)
