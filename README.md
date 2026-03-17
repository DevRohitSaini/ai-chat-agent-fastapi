# 🤖 AI Agent Backend (FastAPI)

A multi-user AI agent backend built using FastAPI with clean architecture, dependency injection, and async-ready design.

---

## 🚀 Features

* ⚡ FastAPI-based REST API
* 👥 Multi-user agent support
* 🧠 In-memory conversation history
* 🔌 Dependency Injection (DI)
* 🔄 Async-ready architecture
* 🧱 Clean code structure (Service Layer + Agent Layer)

---

## 📁 Project Structure

```
.
├── main.py              # FastAPI application
├── agent_manager.py     # Manages multiple agents
├── chatAgent.py         # AI Agent logic
└── README.md
```

---

## 🧠 How It Works

* Each user has a dedicated `ChatAgent`
* Agents are managed by `AgentManager`
* Conversation history is stored per user
* FastAPI handles API routing and dependency injection

---

## 📌 API Endpoints

### 1. Chat with Agent

**POST** `/chat`

#### Request Body:

```json
{
  "name": "john",
  "message": "Hello"
}
```

#### Response:

```json
{
  "response": "Hello john, your message is : Hello",
  "memory": [...]
}
```

---

### 2. Get Chat History

**GET** `/history/{name}`

#### Response:

```json
{
  "memory": [...]
}
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ai-agent-fastapi.git
cd ai-agent-fastapi

pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🔮 Future Improvements

* ✅ Integrate LLM (OpenAI API)
* ✅ Persistent storage (Database)
* ✅ Authentication system
* ✅ Streaming responses
* ✅ Docker deployment

---

## 🧑‍💻 Tech Stack

* Python
* FastAPI
* Pydantic

---

## 📈 Learning Goals

This project demonstrates:

* Backend API development
* OOP design
* Dependency Injection
* Async programming
* Multi-user state management

---

## ⭐ Contribute / Support

If you found this useful, consider giving a ⭐ on GitHub!

---
