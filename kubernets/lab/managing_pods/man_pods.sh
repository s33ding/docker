#!/bin/bash

# Function to make a pod inactive
make_pod_inactive() {
    read -p "Is the pod part of a deployment? (yes/no): " is_deployment
    if [ "$is_deployment" == "yes" ]; then
        read -p "Enter the deployment name: " deployment_name
        kubectl scale deployment "$deployment_name" --replicas=0
    else
        read -p "Enter the pod name to delete: " pod_name
        kubectl delete pod "$pod_name"
    fi
}

# Function to delete specific pods
delete_pods() {
    read -p "Enter the names of the pods to delete (space-separated): " pod_names
    kubectl delete pod $pod_names
}

# Main script
echo "Manage Kubernetes Pods"
echo "======================"

# Make a pod inactive
echo "Make a Pod Inactive"
make_pod_inactive

# Delete specific pods
echo "Delete Specific Pods"
delete_pods

echo "Operations completed."

