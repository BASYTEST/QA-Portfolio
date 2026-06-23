import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

assert response.status_code == 200

data = response.json()

assert data["userId"] == 1
assert data["id"] == 1

print("Test passed")
