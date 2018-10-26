# Use an official Python runtime as a parent image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /rec

# Copy the current directory contents into the container at /app
ADD . /rec

RUN apt-get update
RUN apt-get install -y python3-pip apache2

RUN pip3 install --upgrade --trusted-host pypi.python.org setuptools -r requirements.txt

RUN cd rec && pip3 install -e ".[testing]"

# Make port 6543 available to the world outside this container
EXPOSE 6543

# Run app.py when the container launches
CMD cd rec && pserve --reload --verbose development.ini
