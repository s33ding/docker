IMG_NM="fedora"
CONTAINER_NM="my-$IMG_NM"

docker run -it -p 7777:7777 -v $(pwd):/home/$USER --name $CONTAINER_NM $IMG_NM bash
docker start $CONTAINER_NM 

