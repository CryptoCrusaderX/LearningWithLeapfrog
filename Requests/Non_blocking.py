import requests
from requests_futures.sessions import FuturesSession
import time

session = FuturesSession()
start = time.time()

futures = [
    session.get("https://httpbin.org/delay/2"),
    session.get("https://httpbin.org/delay/2"),
]

for future in futures:
    response = future.result()
    print(response.status_code)

print("Finished in", time.time() - start, "seconds")
