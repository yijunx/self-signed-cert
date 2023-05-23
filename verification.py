import requests, os


os.environ["REQUESTS_CA_BUNDLE"] = "certs/ssl.pem"
r = requests.get("https://cool.domain.yolo")
assert r.status_code == 200


