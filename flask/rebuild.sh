docker rm -f flask
docker rmi img-flask
sudo docker build . -t img-flask
sudo docker run --name flask -d -p 8000:8000 --restart unless-stopped img-flask

