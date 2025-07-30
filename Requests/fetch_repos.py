import requests
import time


def fetch_all_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=30"
    repos = []
    page = 1

    while url:
        print(f"Fetching page {page}...")
        response = requests.get(url)
        if response.status_code != 200:
            print(
                f"Error fetching page {page}: {response.status_code} - {response.reason}"
            )
            break

        data = response.json()
        if not data:
            print("No more repositories found.")
            break

        repos.extend([repo["name"] for repo in data])

        next_link = response.links.get("next", {}).get("url")
        url = next_link
        page += 1

        # Be kind to GitHub API, avoid hitting rate limits
        time.sleep(1)

    return repos


def main():
    username = input("Enter GitHub username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    print(f"\nStarting repo fetch for user: {username}\n")
    repos = fetch_all_repos(username)

    print(f"\nFetched {len(repos)} repositories for user '{username}':")
    for idx, repo_name in enumerate(repos, 1):
        print(f"{idx}. {repo_name}")


if __name__ == "__main__":
    main()
