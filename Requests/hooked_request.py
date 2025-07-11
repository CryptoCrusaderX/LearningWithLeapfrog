import requests

url = "https://httpbin.org/get"


def custom_get(url, hooks=None):
    print(f"Sending GET requests to:{url}")
    response = requests.get()

    if hooks:
        for hook in hooks:
            try:
                hook(response)
            except Exception as e:
                print(f"Error in hooks:{e}")

    return response


def print_url_hook(resp):
    print("Hook Triggered. URL was:", resp.url)


def check_status_hook(resp):
    if resp.status_code == 200:
        print("Status OK(200)")
    else:
        print("Something went Wrong!")


if __name__ == "__main__":
    response = custom_get(
        "https://httpbin.org/get", hooks=[print_url_hook, check_status_hook]
    )

    print("Response content length:", len(response.text))
