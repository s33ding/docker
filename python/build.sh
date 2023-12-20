NAME="pyscript"
IMG="img-$NAME"

sudo docker build . -t $IMG
sudo docker run --name $NAME -d -p 9000:6000 --restart unless-stopped $IMG
