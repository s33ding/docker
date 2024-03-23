IMG_NM="ubuntu"
CONTAINER_NM="my-$IMG_NM"

# Run a Docker container with Ubuntu
docker run -it -p 6666:6666 -v $(pwd):/home/$USER --name $CONTAINER_NM $IMG_NM bash -c "
    # Install Docker inside the container
    apt-get update -y && apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
    apt-get update -y && apt-get install -y docker.io
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

    # Start a bash shell
    bash
"


