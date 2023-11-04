CONTAINER_NAME="my-hadoop"
IMAGE_NAME="suhothayan/hadoop-spark-pig-hive:2.9.2"
docker run -it -d --name $CONTAINER_NAME -v $(pwd):/home/$USER/hadoop $IMAGE_NAME
