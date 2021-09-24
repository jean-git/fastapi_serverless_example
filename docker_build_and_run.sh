#!/bin/bash

APP_NAME=fastapi-app
IMAGE_NAME=$APP_NAME
CONTAINER_NAME=$APP_NAME

docker rm --force $CONTAINER_NAME
docker build -t $IMAGE_NAME .
docker run -d --name $CONTAINER_NAME -v $(pwd)/app:/app --restart=always -p 8000:8000 $IMAGE_NAME

#docker logs $CONTAINER_NAME
#docker ps
#sleep 5
#curl http://localhost:8081

