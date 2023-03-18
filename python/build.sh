sudo docker build . -t img-pyScript
sudo docker run --name pyScript -d -p 9000:6000 --restart unless-stopped img-pyScript