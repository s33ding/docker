# Use the official TensorFlow Docker image as base
FROM tensorflow/tensorflow:latest-jupyter

# Update and install Vim
RUN apt-get update && \
    apt-get install -y vim && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
# Install Python dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Define the working directory
WORKDIR /workspace

