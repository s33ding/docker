source .env

docker rm $CONTAINER_NAME -f
docker rmi $IMG_NAME -f
