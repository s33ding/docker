#!/bin/bash

export AIRFLOW__LOGGING__REMOTE_LOGGING=False
export AIRFLOW__ELASTICSEARCH__HOST=


docker compose down &&\
docker rmi -f $(docker images -q) &&\
docker compose up -d

