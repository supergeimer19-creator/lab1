import requests

def test_requests():
    response = requests.get("https://api.github.com")
    print(f"requests: Статус запиту до GitHub API -> {response.status_code}")