import requests
headers = {
        "Accept" : "application/vnd.github.v3+json",
}

response = requests.post('https://github.com/users/pgDora56/contributions', headers=headers)
print(response.text)
