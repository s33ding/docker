from config import REGION, REPOSITORY_NAME, IMAGE_NAME, TAG
from shared_func.ecr_func import delete_ecr_repository, create_ecr_repository, get_ecr_login_password

if __name__ == "__main__":
    # Create ECR repository
    response = delete_ecr_repository(REGION, REPOSITORY_NAME)
    print(f"Repository {REPOSITORY_NAME} deleted in region {REGION}")
    print(response)
