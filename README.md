# docker-http-server

A simple example of how to run a docker application with embedded healtchecks

## How to build it

docker build -t docker-http-server .

## How to run it
docker run --rm -it --name my-docker-instance -p 8080:8080 docker-http-server