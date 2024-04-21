#!/bin/bash

source .env

echo "cluster name: $CLUSTER_NAME"
echo "region: $REGION"
echo "nodes name: $NODES_NAME"

while true; do
    echo "1) Create EKS Cluster"
    echo "2) Delete EKS Cluster"
    echo "3) Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            eksctl create cluster --name "$CLUSTER_NAME" --region "$REGION" \
		--zones us-east-1a,us-east-1b,us-east-1c \
		--nodegroup-name "$NODES_NAME" --node-type t2.micro --nodes 2 --node-zones us-east-1a,us-east-1b

            ;;
        2)
            eksctl delete cluster --name "$CLUSTER_NAME" --region "$REGION"
            ;;
        3)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option, please try again."
            ;;
    esac
done
