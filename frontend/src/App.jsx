import { useState, useEffect } from "react";
import "./App.css";
import React from "react";

function App() {
  // ====== Workflow State ======
  const [owner, setOwner] = useState("");
  const [repo, setRepo] = useState("");
  const [commits, setCommits] = useState([]);
  const [issues, setIssues] = useState([]);

  // ====== AI Docs/Tests State ======
  const [codeInput, setCodeInput] = useState("");
  const [docs, setDocs] = useState("");
  const [tests, setTests] = useState("");

  // ====== Notification State ======
  const [workflowNotif, setWorkflowNotif] = useState("");
  const [codeNotif, setCodeNotif] = useState("");

  // ====== Helper: Save text to file ======
  const saveToFile = (content, filename) => {
    const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  // ====== Splash Screen ======
  const [showSplash, setShowSplash] = useState(true);
  useEffect(() => {
    const t = setTimeout(() => setShowSplash(false), 5500); 
    return () => clearTimeout(t);
  }, []);

  // ====== Fetch GitHub Commits ======
  const fetchCommits = async () => {
    if (!owner.trim() || !repo.trim()) {
      setWorkflowNotif("⚠ Please enter owner and repo first.");
      setCommits([]);
      setTimeout(() => setWorkflowNotif(""), 3000);
      return;
    }
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/github/commits?owner=${owner}&repo=${repo}`
      );
      const data = await res.json();
      setCommits(data.commits || []);
    } catch (err) {
      console.error("Error fetching commits:", err);
      setCommits([]);
    }
  };

  // ====== Fetch GitHub Issues ======
  const fetchIssues = async () => {
    if (!owner.trim() || !repo.trim()) {
      setWorkflowNotif("⚠ Please enter owner and repo first.");
      setIssues([]);
      setTimeout(() => setWorkflowNotif(""), 3000);
      return;
    }
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/github/issues?owner=${owner}&repo=${repo}`
      );
      const data = await res.json();
      setIssues(data.issues || []);
    } catch (err) {
      console.error("Error fetching issues:", err);
      setIssues([]);
    }
  };

  // ====== Generate Docs via LM Studio ======
  const generateDocs = async () => {
    if (!codeInput.trim()) {
      setCodeNotif("⚠ Please enter some code first.");
      setDocs("");
      setTimeout(() => setCodeNotif(""), 3000);
      return;
    }
    try {
      const res = await fetch("http://127.0.0.1:8000/generate/docs", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: codeInput }),
      });
      if (!res.ok) {
        const text = await res.text();
        throw new Error(`HTTP ${res.status}: ${text}`);
      }
      const data = await res.json();
      setDocs(data.docs || "⚠ No docs returned from LM Studio");
    } catch (err) {
      console.error("Error generating docs:", err);
      setDocs(`❌ Error generating docs: ${err.message}`);
    }
  };

  // ====== Generate Tests via LM Studio ======
  const generateTests = async () => {
    if (!codeInput.trim()) {
      setCodeNotif("⚠ Please enter some code first.");
      setTests("");
      setTimeout(() => setCodeNotif(""), 3000);
      return;
    }
    try {
      const res = await fetch("http://127.0.0.1:8000/generate/tests", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: codeInput }),
      });
      if (!res.ok) {
        const text = await res.text();
        throw new Error(`HTTP ${res.status}: ${text}`);
      }
      const data = await res.json();
      setTests(data.tests || "⚠ No tests returned from LM Studio");
    } catch (err) {
      console.error("Error generating tests:", err);
      setTests(`❌ Error generating tests: ${err.message}`);
    }
  };

  return (
    <div className="App">
      {/* ====== Splash Screen ====== */}
      {showSplash && (
        <div className="splash" role="dialog" aria-label="Loading DevBoost">
          <div className="splash-card">
            <span className="rocket" aria-hidden="true">🚀</span>
            <h1>DevBoost</h1>
            <div className="feature-cards">
              <div className="feature-card" style={{ animationDelay: "0.5s" }}>
                Centralizes developer workflows 
              </div>
              <div className="feature-card" style={{ animationDelay: "1s" }}>
                Auto-generates documentation
              </div>
              <div className="feature-card" style={{ animationDelay: "1.5s" }}>
                Uses AI for test cases 
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ====== Main Dashboard ====== */}
      {!showSplash && (
        <>
          <header className="header">
            <h1><span className="rocket">🚀</span> DevBoost Dashboard</h1>
            <p>"From code to docs to tests—everything under one roof."</p>
          </header>

          <div className="container">
            {/* Workflow Card */}
            <div className="card">
              <h2>📂 Workflow</h2>
              <div className="inputs">
                <input
                  placeholder="Github owner"
                  value={owner}
                  onChange={(e) => setOwner(e.target.value)}
                />
                <input
                  placeholder="Repo name"
                  value={repo}
                  onChange={(e) => setRepo(e.target.value)}
                />
              </div>
              {workflowNotif && <p className="notif">{workflowNotif}</p>}
              <div className="actions">
                <button onClick={fetchCommits}>Fetch Commits</button>
                <button onClick={fetchIssues}>Fetch Issues</button>
                  <button className="clear-btn" onClick={() => {
    setOwner("");
    setRepo("");
    setCommits([]);  // clear commits
    setIssues([]);   // clear issues
  }}>Clear</button>
              </div>

              <h3>Commits</h3>
              <ul className="list">
                {commits.length > 0 ? (
                  commits.map((c) => (
                    <li key={c.sha}>
                      <a href={c.html_url} target="_blank" rel="noreferrer">{c.message}</a>{" "}
                      <span className="meta">— {c.author}</span>
                    </li>
                  ))
                ) : <li>No commits found.</li>}
              </ul>

              <h3>Issues</h3>
              <ul className="list">
                {issues.length > 0 ? (
                  issues.map((i) => (
                    <li key={i.id}>
                      <a href={i.url} target="_blank" rel="noreferrer">{i.title}</a>{" "}
                      <span className="meta">— opened by {i.user}</span>
                    </li>
                  ))
                ) : <li>No issues found.</li>}
              </ul>
            </div>

            {/* AI Docs & Tests Card */}
            <div className="card">
              <h2>🤖 AI Docs & Tests</h2>
              <textarea
                placeholder="Paste your code here..."
                value={codeInput}
                onChange={(e) => setCodeInput(e.target.value)}
                rows={6}
              />
              {codeNotif && <p className="notif">{codeNotif}</p>}
              <div className="actions">
                <button onClick={generateDocs}>Generate Docs</button>
                <button onClick={generateTests}>Generate Tests</button>
                <button className="save-btn" onClick={() => {
                  saveToFile(docs, "docs.txt");
                  saveToFile(tests, "tests.txt");
                }}>Save</button>
                <button className="clear-btn" onClick={() => setCodeInput("")}>Clear</button>
              </div>

              <h3>Docs Output:</h3>
              <pre className="output">{docs}</pre>

              <h3>Tests Output:</h3>
              <pre className="output">{tests}</pre>
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
