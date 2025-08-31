import { useState } from "react";

function Workflow() {
  const [owner, setOwner] = useState("");
  const [repo, setRepo] = useState("");
  const [commits, setCommits] = useState([]);
  const [issues, setIssues] = useState([]);

// Fetch commits
const fetchCommits = async () => {
  const res = await fetch(
    `http://127.0.0.1:8000/github/commits?owner=${owner}&repo=${repo}`
  );
  const data = await res.json();
  setCommits(data.commits || []); // Must match the backend key
};

// Fetch issues
const fetchIssues = async () => {
  const res = await fetch(
    `http://127.0.0.1:8000/github/issues?owner=${owner}&repo=${repo}`
  );
  const data = await res.json();
  setIssues(data.issues || []); // Must match the backend key
};


  // Handler for fetching both
  const fetchData = () => {
    fetchCommits();
    fetchIssues();
  };

  return (
    <div>
      <h2>Workflow Dashboard</h2>
      <div style={{ marginBottom: "1rem" }}>
        <input
          type="text"
          placeholder="GitHub owner"
          value={owner}
          onChange={(e) => setOwner(e.target.value)}
        />
        <input
          type="text"
          placeholder="Repo name"
          value={repo}
          onChange={(e) => setRepo(e.target.value)}
        />
        <button onClick={fetchData}>Fetch Commits & Issues</button>
      </div>

      <div style={{ display: "flex", gap: "2rem" }}>
        <div>
          <h3>Commits</h3>
     <ul>
  {commits.length > 0
    ? commits.map((c) => (
        <li key={c.sha}>
          <a href={c.html_url} target="_blank" rel="noreferrer">
            {c.message}
          </a>{" "}
          - <em>{c.author}</em>
        </li>
      ))
    : <li>No commits found.</li>
  }
</ul>

        </div>

        <div>
          <h3>Issues</h3>
       <ul>
  {issues.length > 0
    ? issues.map((i) => (
        <li key={i.id}>
          <a href={i.url} target="_blank" rel="noreferrer">
            {i.title}
          </a>{" "}
          - <em>open by {i.user}</em>
        </li>
      ))
    : <li>No issues found.</li>
  }
</ul>

        </div>
      </div>
    </div>
  );
}

export default Workflow;

