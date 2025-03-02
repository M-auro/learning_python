"""
Example of using API in Python to list all AWS S3 buckets.
"""

import boto3

def list_buckets(region_name='us-east-1'):
    """
    List all AWS S3 buckets and print their names.
    :param region_name: AWS region name
    """
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3', region_name=region_name)  # Replace 'us-east-1' with your desired region

    # Call S3 to list current buckets
    response = s3.list_buckets()

    # Get a list of all bucket names from the response
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]

    print(f"Bucket List: {bucket_names}")

if __name__ == "__main__":
    list_buckets(region_name='us-east-1')  # You can replace 'us-east-1' with any desired region

