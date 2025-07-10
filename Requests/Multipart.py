import requests

url = "https://httpbin.org/post"
multiple_files = [
    ("images", ("image.jpg", open("image.jpg", "rb"), "image/png")),
    ("texts", ("myfile.txt", open("myfile.txt", "rb"), "image/png")),
]
r = requests.post(url, files=multiple_files)

print(r.text)
