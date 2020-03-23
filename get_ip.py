import requests
response = requests.get('https://httpbin.org/ip')
data = response.json()
print(f"Your IP is {data['origin']}")
