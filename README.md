# Docker

In this repository I will store some Dockerfile and docker-compose to use as templates for future projects.

![Docker Logo](https://logos-download.com/wp-content/uploads/2016/09/Docker_logo-700x588.png)

##### Usefull commands for docker-cli:

- pull image 

  - sudo docker pull mysql

run docker 

> docker run --name ___ -e MYSQL_ROOT_PASSWORD=___ -p 3306:3306 -d mysql

exec mysql with the cli

> sudo docker exec -it ___ mysql -p

restarting container already created

> docker start ___

start new container interactively

> docker container run -it

run additional command in existing container

> docker  container exec -it

see the version of the docker-cli and server

> docker version

Get docker general info

> docker info

See the main commands

> docker

Pull docker images

> sudo docker pull {img name}

run docker 

> docker run --name ___ -e MYSQL_ROOT_PASSWORD=___ -p 3306:3306 -d mysql

see containers running 

> sudo docker ps -a

exec mysql with the cli

> sudo docker exec -it ___ mysql -p

restarting container already created

> docker start ___

