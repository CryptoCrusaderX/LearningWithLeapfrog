import requests

result = requests.get("https://jsonplaceholder.typicode.com/users/", stream=True)
print(result.raw)

print(result.raw.read(10))

with open("nay", "wb") as fd:
    for chunk in result.iter_content(chunk_size=128):
        fd.write(chunk)
