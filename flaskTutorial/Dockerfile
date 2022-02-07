# Python base image
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster


# Label and Maintainer
LABEL description="Docker image for local development of Flask Tutorial"
MAINTAINER david_lingan <linganda@msu.edu>


# Enter Flask application directory
WORKDIR /Users/bumblev/Raspberry-Pi/flaskTutorial

# Setup (or install requirements)
COPY setup.py setup.py
RUN python3 setup.py


# Copy all files from local directory to docker directory
COPY . .


# Run Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


# Terminal Commands
# docker build --tag python-docker .
# docker images
# docker run <IMAGE ID> 
# docker run -d -p 5000:5000 python-docker
# docker ps
# docker stop <container-name>


