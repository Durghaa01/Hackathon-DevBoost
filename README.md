Future Ready Hackathon 2025
🚀 DevBoost

🏷 Title

DevBoost – Smart Workflow & Documentation Assistant for Developers

👥 Team Members and Information

Durghaashini S Ragunathan (Team Lead)

Eng Jia Xuan

Terence Ling Chee Yew

\*\* Students From UCSI University

❗ Problem Statement

Enhancing Developer Productivity & Code Management

Modern software teams face fragmented workflows:
Developers constantly switch between repos, task managers, and documentation tools.
Documentation is often outdated or missing, causing knowledge gaps.
Writing unit tests is time-consuming and often neglected.
These challenges slow down development, reduce collaboration efficiency, and lower overall software quality.

💡 Solution Summary

DevBoost addresses these issues by:

📂 Centralizing Workflows → integrates GitHub repo commits, issues, and collaboration in one place.

📝 Auto-Generated Documentation → extracts clean, structured docs directly from code and comments.

🧪 AI Test Generator (Simulated) → generates test cases for functions/user stories using a local AI model.

📊 Lightweight Insights Dashboard → tracks history of generated docs and tests for continuous improvement.

This reduces context switching, ensures documentation is always up to date, and encourages better testing practices — all within a single platform.

📌 Project Description

Fast-paced development teams often face scattered workflows, missing documentation, and poor test coverage. These inefficiencies slow down delivery, create knowledge gaps, and increase the risk of bugs.
DevBoost is a web app that centralizes developer workflows, connects directly with GitHub, and uses AI (simulated for demo) to auto-generate both documentation and unit tests. By combining repo insights, instant docs, and test generation into one platform, DevBoost boosts productivity, improves collaboration, and ensures higher code quality.

⚠️ Note

This project was developed as part of a hackathon. It is a functional prototype showcasing the core idea and workflows. For real-world, production-level usage, it will need further enhancements in scalability, security, and deployment.

🛠 Tech Stack

Frontend: React.js (Next.js)
Backend: FastAPI (Python)
AI Service (Simulated): LM Studio (local LLM)
APIs/Tools: GitHub API, Postman for testing
Database: SQLite (for demo metadata storage)

⚡ Setup Instructions

Prerequisites

- Node.js & npm
- Python 3.10+
- LM Studio installed & running locally

Run the Services

1. Start LM Studio

- Run model at 127.0.0.1:1234

2. Backend (FastAPI)

- cd backend
- uvicorn main:app --reload --port 8000
- Runs at 127.0.0.1:8000

3. Frontend (React/Next.js)

- cd frontend
- npm install
- npm run dev
- Runs at 127.0.0.1:3000

4. Open the browser at http://localhost:3000 🎉

💡 Reflections & Learnings

Centralizing tools can drastically reduce context-switching overhead for developers.

AI-powered documentation & test generation, even in a simulated demo, showcased strong potential to save engineering hours.

Integration with existing dev tools (GitHub API, task trackers) is crucial for adoption.

Hackathon takeaway: A strong problem-solution fit is often more impactful than perfect code.
