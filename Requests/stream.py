import requests
import json


url = "https://httpbin.org/stream/10"

response = requests.get(url, stream=True)


if response.encoding is None:
    response.encoding = "utf-8"

print("Streaming response line by line...\n")


for line in response.iter_lines(decode_unicode=True):
    if line:
        data = json.loads(line)
        print(f"Received: {data}")
