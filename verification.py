import requests


r = requests.get("https://YOUR_DOMAIN_NAME")
r.raise_for_status()
print(r.text)

