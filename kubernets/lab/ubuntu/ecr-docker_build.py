from config import REGION, REPOSITORY_NAME, IMAGE_NAME, TAG, REGISTRY
from shared_func.ecr_func import *

if __name__ == "__main__":
    docker_build(IMAGE_NAME)
