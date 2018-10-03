# Use an official Python runtime as a parent image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /rec

# Copy the current directory contents into the container at /app
ADD . /rec

RUN apt-get update
RUN apt-get install -y python3-pip python3-venv apache2

RUN python3 -m venv ~/env
RUN ~/env/bin/pip3 install --upgrade --trusted-host pypi.python.org setuptools -r requirements.txt

RUN cd rec && ~/env/bin/pip3 install -e ".[testing]"

RUN cd rec && ~/env/bin/pytest

# Make port 6543 available to the world outside this container
EXPOSE 6543
	
# Run app.py when the container launches
CMD cd rec && ~/env/bin/pserve development.ini
