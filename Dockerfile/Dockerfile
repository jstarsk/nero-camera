FROM ubuntu:18.04

MAINTAINER Starsky Lara "starsk@noumena.io"

# Install software
RUN apt-get update && apt-get install -y nano && apt-get install -y git && apt-get install -y apt-utils && apt-get install -y python-dev python-pip

RUN pip install serial

RUN git clone https://github.com/Parrot-Developers/sequoia-ptpy.git
WORKDIR /sequoia-ptpy
RUN python setup.py install

WORKDIR /

RUN git clone https://github.com/jstarsk/nero-camera.git