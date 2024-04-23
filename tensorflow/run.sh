#!/bin/bash

# Source environment variables
source .env

# Run Docker container with provided arguments
docker run -it -p "$CONTAINER_PORT" -v "$(pwd)/exerc:/tf" --name "$CONTAINER_NAME" "$IMG_NAME"
