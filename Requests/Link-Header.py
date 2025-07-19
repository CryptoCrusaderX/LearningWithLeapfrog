import requests

url = "https://api.github.com/users/kennethreitz/repos?per_page=5"
r = requests.get(url)

print("Links:", r.links)

if "next" in r.links:
    print("Next Page URL:", r.links["next"]["url"])
