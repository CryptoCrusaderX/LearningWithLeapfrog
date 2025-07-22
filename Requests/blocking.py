import requests
import time

start = time.time()

for url in ["https://httpbin.org/delay/2", "https://httpbin.org/delay/2"]:
    response = requests.get(url)
    print(response.status_code)

print("Finished in", time.time() - start, "seconds")
