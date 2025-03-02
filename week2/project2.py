# Write a script that list running k8s pods in a given namespace using the Kubernetes API in Python.
#
# The script should have the following functions:
#
# list_pods(namespace)
# This function should list all running pods in the given namespace.
#
# The script should be able to run as a standalone script and list all running pods in the default namespace.
#
# The script should be able to run as a standalone script and list all running pods in a given namespace.
#
# The script should be able to run as a module and list all running pods in the default namespace.
#

import os
from kubernetes import client, config # Import the required libraries

def list_running_pods (namespace):
    """
    List all running pods in a given namespace.
    :param namespace: Kubernetes namespace
    """
    # Load the Kubernetes configuration file
    config.load_kube_config()

    # Create an instance of the Kubernetes API client
    v1 = client.CoreV1Api()

    # List all running pods in the given namespace
    pods = v1.list_namespaced_pod(namespace)

    # Get a list of all running pod names from the response
    pod_names = [pod.metadata.name for pod in pods.items]

    print(f"Running Pods in Namespace {namespace}: {pod_names}")

if __name__ == "__main__":
    # Check if the KUBERNETES_NAMESPACE environment variable is set
    namespace = os.getenv("KUBERNETES_NAMESPACE")

    if namespace:
        list_running_pods(namespace)
    else:
        list_running_pods("default") # List all running pods in the default namespace
