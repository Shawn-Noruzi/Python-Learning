import json
import requests


headers = {"Content-Type": "application/json"}
url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longurl":"http://example.com"}

response = requests.post(url, json=payload, headers=headers)


print(response.status_code)
print(response.json())
