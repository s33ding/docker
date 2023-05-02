sudo docker build . -t img-pyScript
sudo docker run --name pyscript -d -p 9000:6000 --restart unless-stopped img-pyScript
