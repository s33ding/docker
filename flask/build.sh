sudo docker build . -t img-flask
sudo docker run --name flask -d -p 8000:8000 --restart unless-stopped img-flask

