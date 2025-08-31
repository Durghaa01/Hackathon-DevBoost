import httpx
import os

print(">>> github_service.py LOADED <<<")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BASE_URL = "https://api.github.com"
headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# Fetch commits and simplify
async def get_commits(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    async with httpx.AsyncClient(follow_redirects=True, timeout=15.0) as client:
        r = await client.get(url, headers=headers)
        r.raise_for_status()
        commits = r.json()
        simplified = []
        for c in commits:
            simplified.append({
                "sha": c.get("sha")[:7],
                "message": c.get("commit", {}).get("message", "").split("\n")[0],
                "author": c.get("commit", {}).get("author", {}).get("name"),
                "html_url": c.get("html_url"),
            })
        return simplified

# Fetch issues and simplify
async def get_issues(owner: str, repo: str, state="open"):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues?state={state}"
    async with httpx.AsyncClient(follow_redirects=True, timeout=15.0) as client:
        r = await client.get(url, headers=headers)
        r.raise_for_status()
        issues = r.json()
        simplified = []
        for i in issues:
            # Skip pull requests
            if "pull_request" in i:
                continue
            simplified.append({
                "id": i.get("number"),
                "title": i.get("title"),
                "state": i.get("state"),
                "created_at": i.get("created_at"),
                "url": i.get("html_url"),
                "user": i.get("user", {}).get("login"),
            })
        return simplified
