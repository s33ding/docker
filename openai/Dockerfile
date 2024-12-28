# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y vim  openvpn && \
    rm -rf /var/lib/apt/lists/*

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Copy the rest of the application code
COPY . .

# Copy just the requirements file
COPY requirements.txt .

# Install pip requirements
RUN python -m pip install -r requirements.txt



# No CMD specified
CMD ["python3","main.py"]
