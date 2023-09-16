NM="my-cassandra"

docker run -it -p 9042:9042 --name $NM -d -v /home/$USER/cassandra/data/node1:/var/lib/cassandra/data cassandra
