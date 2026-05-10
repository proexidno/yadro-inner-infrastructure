#!/bin/bash

docker build -t proexidno/yadro:latest . && \
docker run --name yadro-test -d proexidno/yadro:latest && \
sleep 10 && \
docker logs yadro-test > ./docker-artifact/docker.log
