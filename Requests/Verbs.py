import requests
import json

issue_url = "https://api.github.com/repos/psf/requests/issues/482"
response = requests.get(issue_url)


print("Status Code:", response.status_code)

if response.status_code == 200:
    issue_data = response.json()
    print("Issue Title:", issue_data["title"])
    print("Number of Comments:", issue_data["comments"])

    comments_url = issue_url + "/comments"
    comments_response = requests.get(comments_url)

    if comments_response.ok:
        comments = comments_response.json()
        for i, comment in enumerate(comments, start=1):
            print(f"\nComment {i} by {comment['user']['login']}:")
            print(comment["body"])
else:
    print("Issue not found or API limit reached.")
