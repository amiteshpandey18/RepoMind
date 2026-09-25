# RepoMind

RepoMind is an AI-powered GitHub repository assistant that helps developers understand and explore code repositories using natural language.

Instead of manually searching through files, commits, issues, and pull requests, users can connect a GitHub repository and ask questions about the project.

RepoMind uses **RAG, ChromaDB, MCP, and LangGraph** to retrieve relevant repository information and generate contextual answers.

---

## Features

- 🔐 User registration and JWT authentication
- 🔗 Connect any GitHub repository
- 📁 Explore repository files and folders
- 🔍 Semantic search across repository code
- 🤖 AI-powered repository question answering
- 🧠 RAG-based code retrieval
- 📚 ChromaDB vector database
- 🔧 MCP tools for repository information
- 🧩 LangGraph-based agent workflow
- 💬 Conversation memory
- 💾 PostgreSQL persistence for LangGraph conversations
- 📝 GitHub commit history
- 🐛 GitHub issues
- 🔀 GitHub pull requests
- 📌 Source file references in AI answers
- ⚡ Streaming AI responses
- 🎨 React-based frontend
- 🔄 Repository indexing only when required

---

## How RepoMind Works

The basic flow is:

```text
User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
LangGraph Agent
  ↓
Tool Selection
  ↓
MCP Tools
  ↓
┌─────────────────────────────┐
│ Repository Search           │
│ Commits                     │
│ Issues                      │
│ Pull Requests               │
└─────────────────────────────┘
  ↓
RAG / ChromaDB
  ↓
Relevant Repository Context
  ↓
OpenAI
  ↓
Streaming Answer


Tech Stack
Backend
Python
FastAPI
PostgreSQL
SQLAlchemy
JWT
HTTPX
AI
OpenAI
LangGraph
MCP
ChromaDB
RAG
OpenAI Embeddings
Frontend
React
JavaScript
React Markdown
CSS
Tools
Git
GitHub API
Postman
uv


Project Structure

RepoMind/
│
├── backend/
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── src/
│       └── repomind/
│           ├── main.py
│           ├── api/
│           ├── auth/
│           ├── core/
│           ├── db/
│           ├── rag/
│           ├── services/
│           ├── agent/
│           └── mcp/
│
├── frontend/
│   └── src/
│
├── .gitignore
├── .python-version
└── README.md



RAG Pipeline

RepoMind uses Retrieval-Augmented Generation to understand repository code.

GitHub Repository
       ↓
Repository Files
       ↓
File Content
       ↓
Code Chunks
       ↓
OpenAI Embeddings
       ↓
ChromaDB
       ↓
Semantic Search
       ↓
Relevant Code
       ↓
OpenAI
       ↓
AI Answer

Repository chunks are stored in ChromaDB along with metadata such as:

file
owner
repo

This allows RepoMind to search only within the connected repository.

LangGraph Agent

LangGraph is used to decide which tool should handle the user's question.

User Question
      ↓
LangGraph Agent
      ↓
Tool Selection
      ↓
┌─────────────────────────┐
│ search_repository       │
│ get_commits             │
│ get_issues              │
│ get_pull_requests       │
└─────────────────────────┘
      ↓
Repository Context
      ↓
OpenAI
      ↓
AI Answer

For example:

"How does authentication work?"
        ↓
search_repository
"What are the recent commits?"
        ↓
get_commits
"What issues are open?"
        ↓
get_issues
"What pull requests exist?"
        ↓
get_pull_requests
MCP

RepoMind uses MCP to expose repository operations as tools.

Available MCP tools:

search_repository
get_commits
get_issues
get_pull_requests

LangGraph selects the appropriate MCP tool based on the user's question.

Conversation Memory

RepoMind uses PostgreSQL with the LangGraph PostgreSQL checkpointer to persist conversation state.

User Conversation
       ↓
LangGraph
       ↓
PostgreSQL
       ↓
Persistent Conversation State

This allows conversation state to remain available even after the backend is restarted.

Authentication

RepoMind provides JWT-based authentication.

Register
   ↓
Password Hashing
   ↓
PostgreSQL

Login
   ↓
Password Verification
   ↓
JWT Token
   ↓
Authenticated User

Authentication endpoints:

POST /auth/register
POST /auth/login
GET  /auth/me
API Endpoints
Health Check
GET /health
Repository Information
GET /github/{owner}/{repo}
Repository Files
GET /github/{owner}/{repo}/files
Repository Folder
GET /github/{owner}/{repo}/files/{path}
Repository File
GET /github/{owner}/{repo}/file/{path}
Repository Commits
GET /github/{owner}/{repo}/commits
Authentication
POST /auth/register
POST /auth/login
GET  /auth/me
Example Questions

After connecting a GitHub repository, users can ask:

How does authentication work?
How is the database configured?
How does the payment system work?
What are the recent commits?
What issues are currently open?
What pull requests exist?
Which files implement the reservation system?

RepoMind retrieves relevant repository information before generating the answer.

Environment Variables

Create a .env file inside the backend directory.

DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/repomind

OPENAI_API_KEY=your_openai_api_key

GITHUB_TOKEN=your_github_token

SECRET_KEY=your_secret_key

Do not commit the .env file to GitHub.



Current Status
Completed
 FastAPI backend
 React frontend
 PostgreSQL database
 JWT authentication
 GitHub API integration
 Repository explorer
 Repository indexing
 Code chunking
 OpenAI embeddings
 ChromaDB vector search
 RAG-based repository search
 MCP server
 MCP client
 LangGraph agent
 Tool routing
 Commit search
 Issue search
 Pull request search
 Streaming AI responses
 Source file references
 Conversation memory
 PostgreSQL LangGraph persistence
 Repository re-indexing prevention


## Future Improvements

- [ ] Improve security configuration
- [ ] Add more automated tests
- [ ] Improve issue and pull request UI
- [ ] Improve error handling
- [ ] Add more repository analysis tools
- [ ] Add repository branch selection
- [ ] Improve conversation history UI
- [ ] Expand Agentic AI capabilities
- [ ] Deploy the application






















  ↓
React
UI
