import requests

requests_bbc = requests.get("https://bbc.co.uk/")

#print(requests_bbc)

print(requests_bbc.content)

