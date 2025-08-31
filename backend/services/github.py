import os, requests

GH_API = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def _headers():
    h = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return h

def get_commits(owner: str, repo: str, per_page: int = 10):
    url = f"{GH_API}/repos/{owner}/{repo}/commits?per_page={per_page}"
    r = requests.get(url, headers=_headers(), timeout=15)
    r.raise_for_status()
    data = r.json()
    return [{
        "sha": c.get("sha")[:7],
        "message": (c.get("commit", {}).get("message","") or "").split("\n")[0],
        "author": (c.get("commit", {}).get("author", {}).get("name") or c.get("author",{}).get("login")),
        "date": c.get("commit", {}).get("author", {}).get("date")
    } for c in data]

def get_issues(owner: str, repo: str, state="open", per_page: int = 10):
    url = f"{GH_API}/repos/{owner}/{repo}/issues?state={state}&per_page={per_page}"
    r = requests.get(url, headers=_headers(), timeout=15)
    r.raise_for_status()
    data = r.json()
    issues = [i for i in data if "pull_request" not in i]
    return [{"id": i["number"], "title": i["title"], "user": i["user"]["login"], "created_at": i["created_at"]} for i in issues]
