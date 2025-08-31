from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from services import github_service
from services.openai_service import generate_docs, generate_tests

app = FastAPI(title="DevBoost API")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in dev allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/")
def root():
    return {"message": "🚀 DevBoost API is running!"}


# ===== GitHub Endpoints (async) =====
@app.get("/github/commits")
async def fetch_commits(owner: str = Query(...), repo: str = Query(...)):
    try:
        commits = await github_service.get_commits(owner, repo)
        return {"commits": commits}
    except Exception as e:
        print(f"Error fetching commits for {owner}/{repo}: {e}")
        return {"commits": []}


@app.get("/github/issues")
async def fetch_issues(owner: str = Query(...), repo: str = Query(...)):
    try:
        issues = await github_service.get_issues(owner, repo)
        return {"issues": issues}
    except Exception as e:
        print(f"Error fetching issues for {owner}/{repo}: {e}")
        return {"issues": []}


# ===== Docs/Tests Endpoints (async) =====
@app.post("/generate/docs")
async def docs_endpoint(request: Request):
    body = await request.json()
    code = body.get("code", "")
    docs = await generate_docs(code)
    return {"docs": docs or "No docs generated."}


@app.post("/generate/tests")
async def tests_endpoint(request: Request):
    body = await request.json()
    code = body.get("code", "")
    tests = await generate_tests(code)
    return {"tests": tests or "No tests generated."}
