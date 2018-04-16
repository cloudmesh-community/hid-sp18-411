FROM python:2.7

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y mongodb-clients psmisc
EXPOSE 8080

WORKDIR /docker/default_controller/
COPY ./server/ /docker/default_controller/
RUN pip install -r requirements.txt
COPY ./build_docker.sh build_docker.sh
RUN chmod +x /docker/default_controller/build_docker.sh