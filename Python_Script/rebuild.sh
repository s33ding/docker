docker rm -f bot-dev
docker rmi img-bot-dev
sudo docker build . -t img-bot-dev
sudo docker run --name bot-dev -d -p 9000:6000 --restart unless-stopped img-bot-dev