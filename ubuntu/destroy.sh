IMG_NM="ubuntu"
CONTAINER_NM="my-$IMG_NM"

docker stop $CONTAINER_NM
docker rm $CONTAINER_NM
