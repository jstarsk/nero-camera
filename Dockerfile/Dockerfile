FROM ubuntu:18.04

MAINTAINER Starsky Lara "starsk@noumena.io"

# Install software
RUN apt-get update && apt-get install -y git && apt-get install -y apt-utils && apt-get install -y python-dev python-pip

# Make ssh dir
RUN mkdir /root/.ssh/

# Copy over private key, and set permissions
ADD $HOME/ssh/id_rsa /root/.ssh/id_rsa

# Create known_hosts
RUN touch /root/.ssh/known_hosts
# Add bitbuckets key
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts

# Clone the conf files into the docker container
RUN git clone git@bitbucket.org:jstarsky/nero-camera.git