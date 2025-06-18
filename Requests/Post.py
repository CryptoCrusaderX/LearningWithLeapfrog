import requests

payload_tuples = [("key1", "value1"), ("key2", "value2")]

r1 = requests.post("https://httpbin.org/post", data=payload_tuples)

payload_dict = {"key": ["value1", "value2"]}

r2 = requests.post("https://httpbin.org/post", data=payload_dict)

print(r1.text)

if r1.text == r2.text:
    print("TRUE")
else:
    print("False")
