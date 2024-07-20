from config import REGION, REPOSITORY_NAME, IMAGE_NAME, TAG
from shared_func.ecr_func import create_ecr_repository, get_ecr_login_password 

if __name__ == "__main__":
    # Create ECR repository
    response = create_ecr_repository(REGION, REPOSITORY_NAME)
    if response:
        print(f"Repository {REPOSITORY_NAME} created in region {REGION}")
    else:
        print(f"Using existing repository {REPOSITORY_NAME} in region {REGION}")
    
