> see the version of the 

docker-cli and server

> docker version

docker general info

> docker info

see the main commands

> docker

sudo docker 

> pull image 

sudo docker pull mysql

> run docker 

docker run --name ___ -e MYSQL_ROOT_PASSWORD=___ -p 3306:3306 -d mysql

> see containers running 

sudo docker ps -a

> exec mysql with the cli

sudo docker exec -it ___ mysql -p

> restarting container already created

docker start ___


> handling ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)eroo

docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' tisaude