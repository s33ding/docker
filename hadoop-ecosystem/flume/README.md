download flume
https://flume.apache.org/download.html

Descompactar o arquivo:
# tar vfx /home/tsthadoop/apache-flume-1.11.0-bin.tar.gz
Mover o pasta descompactada para o endereço local (aonde estão os outros produtos do Ecossistema):
# mv apache-flume-1.11.0-bin /usr/local/.
Criar um link simbólico para facilitar o acesso:
# cd /usr/local/
# ln -s /usr/local/apache-flume-1.11.0-bin flume
Modificar o arquivo 
# vim /etc/bootstrap.sh

adicionar as 2 linhas seguintes abaixo dos comandos EXPORT:

export FLUME_HOME="/usr/local/flume"
export PATH=$PATH:/usr/local/sqoop/bin:/usr/local/flume/bin
