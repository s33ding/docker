name="tensorflow"
docker pull tensorflow/tensorflow:latest  # Download latest stable image
docker run -it -p 8888:8888 -v $(pwd):/tf --name $name tensorflow/tensorflow:latest-jupyter  # Start Jupyter server 
