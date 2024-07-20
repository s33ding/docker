from config import REGION, REPOSITORY_NAME, IMAGE_NAME, TAG, REGISTRY, USER_NAME
from shared_func.ecr_func import *

if __name__ == "__main__":
    docker_login(REGISTRY, USER_NAME)
