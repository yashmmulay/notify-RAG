# Multilingual Agnostic Chatbot

## Application Overview

This application is a **multilingual document-based question answering system** built using a **Retrieval-Augmented Generation (RAG)** architecture.  
It allows users to ask questions in **any language** and get accurate answers from a **collection of PDF documents** available on the server.

The system runs on a **local network**, enabling multiple users to access the application through a web interface while a single RAG engine continuously processes queries in the background.

---

##  Problem Statement & Solution

###  Problem

- Information is often stored across **multiple PDF documents**
- Searching manually through PDFs is **time-consuming and inefficient**
- Most document QA systems:
  - Work only in **English**
  - Rebuild models for every query
  - Are slow and resource-heavy

---

###  Solution

This application solves the problem by:

- Loading **all PDFs once** at startup
- Converting documents into **vector embeddings**
- Using **semantic search** instead of keyword matching
- Translating **multilingual queries** into English automatically
- Generating **context-aware answers** using an LLM
- Returning responses quickly without restarting the RAG engine

As a result, users can:
- Ask questions in their **native language**
- Get precise answers from large document sets
- Access the system from **any device on the same network**

---

## Technologies Used

### 🔹 Frontend
- HTML
- CSS
- JavaScript

### 🔹 Backend
- Node.js
- Express.js
- CORS

### 🔹 RAG Engine
- Python
- FAISS (Vector Similarity Search)
- Sentence Transformers (Embeddings)
- LangChain Text Splitters
- PyMuPDF (PDF Parsing)

### 🔹 AI & NLP
- Google Gemini (LLM)
- Multilingual Translation (`@vitalets/google-translate-api`)

---

##  Setup Instructions

### 1.1️Clone the Repository
```
git clone https://github.com/shambhuz28/techsprint.git
cd techsprint
```
### 2. Python RAG Setup
```bash
python3 -m venv env
source env/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
### 3. Node.js Setup
```bash
npm install
```

Start the application:
```bash
node server.js
```

Access the Application

On the same machine:

http://localhost:4000
