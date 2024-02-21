FROM python:3.9-slim-buster

WORKDIR /app

COPY . .
RUN apt update && apt install build-essential -y \
	&& pip3 install RPi.GPIO \
	&& pip3 install -r requirements.txt

EXPOSE 80
CMD python3 main.py >> logger/log.info 2>&1
