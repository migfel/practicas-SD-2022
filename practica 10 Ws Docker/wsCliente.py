import requests

data = [
    [1, 2, 3],
    [4, 5, 6]
]

response = requests.post('http://localhost:9002/process', json=data)

print(response.json())
