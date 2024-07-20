import boto3
import base64
import subprocess

def create_ecr_repository(region, repository_name):
    ecr_client = boto3.client('ecr', region_name=region)
    try:
        response = ecr_client.create_repository(
            repositoryName=repository_name
        )
        return response
    except ecr_client.exceptions.RepositoryAlreadyExistsException:
        print(f"Repository {repository_name} already exists.")
        return None

def delete_ecr_repository(region, repository_name):
    ecr_client = boto3.client('ecr', region_name=region)
    response = ecr_client.delete_repository(
        repositoryName=repository_name,
        force=True  # Use force=True to delete the repository even if it contains images
    )
    return response

def get_ecr_login_password(region):
    client = boto3.client('ecr', region_name=region)
    response = client.get_authorization_token()
    auth_data = response['authorizationData'][0]
    token = auth_data['authorizationToken']
    username, password = base64.b64decode(token).decode('utf-8').split(':')
    registry = auth_data['proxyEndpoint'].replace('https://', '')
    return registry, username, password

def docker_login(registry, username):
    login_command = f"aws ecr get-login-password --region us-east-1 | docker login --username {username} --password-stdin {registry}"
    subprocess.run(login_command, shell=True, check=True)

def docker_build(image_name,tag=None):
    build_command = f"docker build -t {image_name} ."
    if tag is not None:
        build_command = f"docker build -t {image_name}:{tag} ."
    subprocess.run(build_command, shell=True, check=True)


def docker_tag(image_name, registry, tag=None):
    tag_command = f"docker tag {image_name}:{tag} {registry}/{image_name}:{tag}"
    if tag is None:
        tag_command = f"docker tag {image_name} {registry}/{image_name}"

    subprocess.run(tag_command, shell=True, check=True)

def docker_push(image_name, registry, tag=None):
    if tag is not None:
        push_command = f"docker push {registry}/{image_name}:{tag}"
    else:
        push_command = f"docker push {registry}/{image_name}"
    subprocess.run(push_command, shell=True, check=True)

