# RepoMind

RepoMind is an AI-powered GitHub repository assistant that helps developers understand and explore code repositories using natural language.

Instead of manually searching through files, commits, issues, and pull requests, users can connect a GitHub repository and ask questions about the project.

RepoMind uses **RAG, ChromaDB, MCP, LangGraph, and OpenAI** to retrieve relevant repository information and generate contextual answers.

---

## Features

- 🔐 User registration and JWT authentication
- 🔗 Connect GitHub repositories
- 📁 Explore repository files and folders
- 🔍 Semantic search across repository code
- 🤖 AI-powered repository question answering
- 🧠 RAG-based code retrieval
- 📚 ChromaDB vector database
- 🔧 MCP tools for repository operations
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
  ↓
React UI

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- HTTPX

### AI & RAG
- OpenAI
- OpenAI Embeddings
- LangGraph
- MCP (Model Context Protocol)
- ChromaDB
- Retrieval-Augmented Generation (RAG)

### Frontend
- React
- JavaScript
- React Markdown
- CSS

### Tools & APIs
- Git
- GitHub REST API
- Postman
- uv

## 📁 Project Structure


RepoMind/
│
├── backend/
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── src/
│       └── repomind/
│           ├── main.py
│           │
│           ├── api/
│           │   ├── routes.py
│           │   └── agent.py
│           │
│           ├── auth/
│           │   ├── routes.py
│           │   ├── schemas.py
│           │   └── security.py
│           │
│           ├── core/
│           │   └── config.py
│           │
│           ├── db/
│           │   ├── database.py
│           │   └── models/
│           │
│           ├── rag/
│           │   ├── embeddings.py
│           │   ├── indexer.py
│           │   ├── repository_loader.py
│           │   ├── splitter.py
│           │   └── vector_store.py
│           │
│           ├── services/
│           │   └── github_service.py
│           │
│           ├── agent/
│           │   └── graph.py
│           │
│           └── mcp/
│               ├── mcp_server.py
│               └── mcp_client.py
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── App.jsx
│       └── ...
│
├── .gitignore
├── .python-version
└── README.md


## 💬 Example Questions

After connecting a GitHub repository, users can ask questions such as:

```text
How does authentication work?

How is the database configured?

How does the payment system work?

What are the recent commits?

What issues are currently open?

What pull requests exist?

Which files implement the reservation system?


## 🚀 Current Status

### ✅ Completed

- FastAPI backend
- React frontend
- PostgreSQL database
- JWT authentication
- GitHub REST API integration
- Repository explorer
- Repository indexing
- Code chunking
- OpenAI embeddings
- ChromaDB vector search
- RAG-based repository search
- MCP server
- MCP client
- LangGraph agent
- Tool routing
- Commit search
- Issue search
- Pull request search
- Streaming AI responses
- Source file references
- Conversation memory
- PostgreSQL LangGraph persistence
- Repository re-indexing prevention

## 🔮 Future Improvements

- Improve security configuration
- Add more automated tests
- Improve issue and pull request UI
- Improve error handling
- Add more repository analysis tools
- Add repository branch selection
- Improve conversation history UI
- Expand Agentic AI capabilities
- Deploy the application








