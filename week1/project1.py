#  Write a script that uses podman to pull and scan a nginx Docker image for vulnerabilities

import subprocess

def pull_docker_image(image_name):
    """
    Pull a docker image from Docker Hub
    """
    try:
        print(f"pulling_image: {image_name}")
        subprocess.run(["podman", "pull", image_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def scan_image(image_name):
    """
    Scan the image for vulnerabilities using trivy
    """
    try:
        print(f"scanning_image: {image_name} for vulnerabilities")
        subprocess.run(["podman", "run", "--rm", "-i", "docker.io/aquasec/trivy", "image", image_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_name = "docker.io/library/nginx:latest" # change this to the image you want to pull and scan
    pull_docker_image(image_name)
    scan_image(image_name)