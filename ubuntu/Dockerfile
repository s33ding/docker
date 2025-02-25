# Use official Ubuntu as base image
FROM ubuntu:latest

# Set non-interactive mode to prevent user prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update and install basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    python3 \
    python3-pip \
    ipython \
    docker.io \
    docker-compose \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws/

# Install Python packages
RUN pip3 install --no-cache-dir pandas boto3

# Set default shell
CMD ["/bin/bash"]

