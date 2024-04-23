#!/bin/bash

# Source environment variables
source .env

# Run Docker container with provided arguments
docker run -it -p "$CONTAINER_PORT" -v "$(pwd)/exerc:/workspace" --name "$CONTAINER_NAME" "$IMG_NAME"
