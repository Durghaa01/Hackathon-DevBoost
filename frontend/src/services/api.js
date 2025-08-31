const BASE_URL = "http://127.0.0.1:8000"; // your backend URL

export async function getCommits(owner, repo) {
  const res = await fetch(`${BASE_URL}/github/commits?owner=${owner}&repo=${repo}`);
  const data = await res.json();
  return data.commits;
}

export async function getIssues(owner, repo) {
  const res = await fetch(`${BASE_URL}/github/issues?owner=${owner}&repo=${repo}`);
  const data = await res.json();
  return data.issues;
}
