NAME="airflow"
IMG="img-$NAME"
PORT="8080:8080"
USER_NAME="s33ding"

docker run --name $NAME -d -p $PORT -v $(pwd):/home/$USER_NAME --restart unless-stopped $IMG
