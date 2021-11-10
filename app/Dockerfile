FROM python:3.10.0-buster

RUN apt-get update
RUN apt-get install -y gcc python3 python3-pip
RUN pip3 install discord.py

WORKDIR /app
CMD python3 app.py
