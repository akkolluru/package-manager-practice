import requests

def get_status():
    res = requests.get("https://api.github.com")
    return res.status_code

if __name__ == "__main__":
    status = get_status()
    print(f"GitHub API status code: {status}")