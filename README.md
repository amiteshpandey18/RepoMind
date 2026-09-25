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
  ↓
React UI
