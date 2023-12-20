
NAME="pyscript"
IMG="img-$NAME"

docker rm -f $NAME
docker rmi $IMG
