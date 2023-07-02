import requests

FILE="./data/requests.json"
URL="http://127.0.0.1:8000/predict" # docker

def test_requests():
    file = open(FILE, "r")
    for line in file:
        response = requests.post(URL, data = line, headers = {"accept": "application/json", "Content-Type": "application/json"})
        assert response.status_code == 200

# test_requests()