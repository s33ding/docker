# Docker

In this repository I will store some Dockerfile and docker-compose to use as templates for future projects.

![Docker Logo](https://logos-download.com/wp-content/uploads/2016/09/Docker_logo-700x588.png)

### Usefull commands for docker-cli:

##### pull image 

  - sudo docker pull mysql

##### run docker 

  - docker run --name ___ -e MYSQL_ROOT_PASSWORD=___ -p 3306:3306 -d mysql

##### exec mysql with the cli

  - sudo docker exec -it ___ mysql -p

##### restarting container already created

  - docker start ___

##### start new container interactively

  - docker container run -it

##### run additional command in existing container

  - docker  container exec -it

##### restarting container already created

  - docker start ___

---------
### Getting information from Docker containers

##### see the version of the docker-cli and server

  - docker version

##### docker general info

  - docker info

##### see the main commands

  - docker

##### see containers running, by default ls only show running containers, use '-a' to list all

  - docker ps -a


  - docker container ls

##### see logs

  - docker logs {container_name}

 ##### see process running

  - docker top {container_name}

##### process list in one container 

  - docker container

##### details of one container config 

  - docker container inspect

##### performance stats for all containers, show metadata about the container (startup config, volumes, networking, etc)

  - docker container stats
-------------
### Network

##### show networks

  - docker network ls

##### inspect network

  - docker network inspect

##### create a network

  - docker network create --driver

##### attach a network to container

  - docker network connect

##### detach a network from container

  - docker network disconnect
--------------
##### REFERENCE:

[Docker CLI - Cheatsheet](https://raw.githubusercontent.com/sangam14/dockercheatsheets/master/dockercheatsheet8.png)
