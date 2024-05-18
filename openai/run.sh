# Source environment variables
source .env

# Start the container with the appropriate settings
docker run -e OPENAI_API_KEY=$KEY_ID -itd --name "$CONTAINER_NAME" -p "$CONTAINER_PORT" -v "$(pwd)/app:/app" "$IMG_NAME" 
