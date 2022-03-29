# Python base image
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster


# Label and Maintainer
LABEL description="Docker image for local development of Flask Tutorial"
MAINTAINER david_lingan <linganda@msu.edu>


# Enter Flask application directory
RUN mkdir /flask_docker
COPY . /flask_docker
WORKDIR /flask_docker

# Setup (or install requirements)
RUN pip3 install flask


# Run Flask app
ENV FLASK_APP=flaskr # current name of flask application
ENV FLASK_ENV=development
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


# Terminal (yml) Commands
# docker build --tag <> .
# docker images
# docker run <IMAGE ID> 
# docker run -d -p 5000:5000 <>
# docker ps
# docker stop <container-name>



# 