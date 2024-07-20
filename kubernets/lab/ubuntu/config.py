# Configuration variables
# AWS region where the ECR repository is located
REGION = 'us-east-1'

# Docker image name
IMAGE_NAME = 'ubuntu-ssh'
REPOSITORY_NAME = IMAGE_NAME

# Docker image tag
TAG = 'latest'

# Name of the ECR repository to be created
USER_NAME = 'AWS'

# Docker image name and tag
TAG = 'latest'

# account id
ACCOUNT_ID = '408411726795'
REGISTRY = f"{ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com"
