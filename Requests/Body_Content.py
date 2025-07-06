import requests

url = "https://github.com/psf/requests/tarball/main"
with requests.get(url, stream=True) as r:
    content_length = r.headers.get("content-length")

    if content_length:
        print(f"Length: {int(content_length)} bytes")
        if int(content_length) < 10_000_000:
            content = r.content
        else:
            print("Too large, skipping download.")
    else:
        print("No content-length header found.")
