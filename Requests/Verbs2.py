import requests
import json


def demo_verbs():
    base = "https://httpbin.org"
    tests = {
        "GET": "/get",
        "POST": "/post",
        "PUT": "/put",
        "PATCH": "/patch",
        "DELETE": "/delete",
        "HEAD": "/get",
        "OPTIONS": "/get",
    }

    for verb, path in tests.items():
        url = base + path
        print(f"\n--- {verb} {path} ---")

        if verb in ("POST", "PUT", "PATCH"):
            payload = {"verb": verb, "message": "Hello, httpbin!"}
            r = requests.request(verb, url, json=payload)
        else:
            r = requests.request(verb, url)

        print("Status:", r.status_code)

        if verb in ("HEAD", "OPTIONS"):
            print("Headers:", dict(r.headers))
        else:
            try:
                print("Response JSON:", json.dumps(r.json(), indent=2))
            except ValueError:
                print("No JSON body")


if __name__ == "__main__":
    demo_verbs()
