"""
This script uses podman to pull and scan a nginx Docker image for vulnerabilities.
"""

import subprocess

def pull_docker_image(image):
    """
    Pull a docker image from Docker Hub
    """
    try:
        print(f"pulling_image: {image}")
        subprocess.run(["podman", "pull", image], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def scan_image(image):
    """
    Scan the image for vulnerabilities using trivy
    """
    try:
        print(f"scanning_image: {image} for vulnerabilities")
        subprocess.run(
            ["podman", "run", "--rm", "-i", "docker.io/aquasec/trivy", "image", image],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    IMAGE_NAME = "docker.io/library/nginx:latest"  # change this to the image you want to pull and scan
    pull_docker_image(IMAGE_NAME)
    scan_image(IMAGE_NAME)
