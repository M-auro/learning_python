# Lesson 2: Python API Basics

## Introduction
In this lesson, we will cover the basics of working with APIs in Python. APIs (Application Programming Interfaces) allow different software applications to communicate with each other. We will learn how to send requests to an API and handle the responses.

## What is an API?
An API is a set of rules that allows one piece of software to interact with another. APIs are commonly used to retrieve data from web services.

## Making API Requests
To interact with an API, we need to send HTTP requests. The most common types of requests are:
- `GET`: Retrieve data from the server.
- `POST`: Send data to the server.
- `PUT`: Update data on the server.
- `DELETE`: Remove data from the server.

## Using the `requests` Library
Python provides a powerful library called `requests` to make HTTP requests. To use it, you need to install it first:
```bash
pip install requests
```

### Example: Making a GET Request
Here is an example of how to make a GET request to an API:
```python
import requests

response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Failed to retrieve data')
```

### Example: Making a POST Request
Here is an example of how to make a POST request to an API:
```python
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://api.example.com/data', json=payload)
if response.status_code == 201:
    print('Data successfully posted')
else:
    print('Failed to post data')
```

## Handling API Responses
API responses usually come in JSON format. You can use the `json()` method of the `requests` library to parse the response:
```python
data = response.json()
```

## Conclusion
In this lesson, we learned the basics of working with APIs in Python. We covered how to make GET and POST requests using the `requests` library and how to handle API responses. In the next lesson, we will dive deeper into more advanced API interactions.
