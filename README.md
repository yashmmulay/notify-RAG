# Multilingual Agnostic Chatbot

A Retrieval-Augmented Generation (RAG) based multilingual document question-answering system that enables users to ask questions in **any language** and receive accurate answers from a collection of PDF documents. The application uses semantic search, automatic translation, and Google Gemini to generate context-aware responses.

---

## Overview

The Multilingual Agnostic Chatbot is designed to simplify information retrieval from multiple PDF documents. Instead of manually searching through documents, users can ask natural language questions in their preferred language and receive relevant answers instantly.

The application runs over a **local network**, allowing multiple users to access it through a web interface while a single RAG engine continuously processes queries in the background.

---

## Features

- Ask questions in **multiple languages**
- Retrieve information from multiple PDF documents
- Semantic search using FAISS vector database
- AI-generated answers using Google Gemini
- Automatic translation of multilingual queries
- Fast responses with preloaded document embeddings
- Simple and responsive web interface
- Multi-user access over a local network

---

## Problem Statement

Finding information across multiple PDF documents is often slow and inefficient.

Traditional document QA systems typically:

- Support only English
- Perform keyword-based searches
- Reload documents for every query
- Consume significant computational resources

---

## Solution

This application addresses these challenges by:

- Loading all PDF documents once during startup
- Converting documents into vector embeddings
- Performing semantic similarity search using FAISS
- Automatically translating multilingual queries into English
- Generating context-aware responses using Google Gemini
- Keeping the RAG engine running continuously for faster response times

As a result, users can:

- Ask questions in their native language
- Retrieve accurate information from large document collections
- Access the system from any device connected to the same local network

---

## Tech Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Node.js
- Express.js
- CORS

### RAG Engine

- Python
- FAISS
- Sentence Transformers
- LangChain Text Splitters
- PyMuPDF

### AI & NLP

- Google Gemini
- @vitalets/google-translate-api

---

## 📂 Project Structure

```
.
├── pdfs/                  # PDF documents
├── frontend/              # HTML, CSS, JavaScript
├── backend/
│   ├── server.js
│   └── routes/
├── rag/
│   ├── app.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── utils.py
├── requirements.txt
├── package.json
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yashmmulay/notify-RAG.git
cd notify-RAG
```

---

### 2. Create a Python Virtual Environment

```bash
python3 -m venv env
```

Activate the environment:

**macOS/Linux**

```bash
source env/bin/activate
```

**Windows**

```bash
env\Scripts\activate
```

---

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Node.js Dependencies

```bash
npm install
```

---

### 5. Configure Environment Variables

Create a `.env` file and add your Google Gemini API key:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

### 6. Start the Backend

```bash
node server.js
```

---

### 7. Start the RAG Engine

Run the Python application responsible for document indexing and retrieval (replace with your actual entry file if different):

```bash
python app.py
```

---

## Access the Application

On the same machine:

```
http://localhost:4000
```

From another device on the same network:

```
http://YOUR_LOCAL_IP:4000
```

Example:

```
http://192.168.1.10:4000
```
---

## Future Enhancements

- Document upload through the web interface
- Chat history
- Voice input support
- User authentication
- Streaming AI responses
- Docker deployment
- Cloud deployment
- Support for additional LLMs

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Vector Databases (FAISS)
- Semantic Search
- Google Gemini API
- Sentence Transformers
- LangChain
- PDF Parsing
- Multilingual Translation
- Node.js & Express Integration
- Full-Stack AI Application Development

---
