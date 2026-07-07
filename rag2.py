import sys
print("PYTHON_STARTED", flush=True)

import os
import fitz
import faiss
import numpy as np

from google import genai
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer



os.environ["GEMINI_API_KEY"] = "YOUR GEMINI KEY"
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def query_llm(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()



def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def load_pdfs_from_directory(directory_path: str):
    docs = []
    for file in os.listdir(directory_path):
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(directory_path, file)
            print(f"Loading: {file}")
            text = extract_text_from_pdf(full_path)
            docs.append({
                "file": file,
                "content": text
            })
    return docs



def split_docs(docs, chunk_size=1500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = []
    for doc in docs:
        splits = splitter.split_text(doc["content"])
        for chunk in splits:
            chunks.append(f"[{doc['file']}] {chunk}")

    return chunks



def build_faiss_index(chunks):
    embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    embeddings = embedder.encode(
        chunks,
        batch_size=32,
        convert_to_numpy=True
    ).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, embedder



def retrieve_chunks(query, index, embedder, chunks, k=3):
    query_vec = embedder.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        similarity = 1 / (1 + dist)
        results.append({
            "text": chunks[idx],
            "confidence": round(similarity * 100, 2)
        })

    return results



def answer_query(user_query, index, embedder, chunks):
    retrieved = retrieve_chunks(user_query, index, embedder, chunks)

    context = "\n\n".join(r["text"] for r in retrieved)
    avg_confidence = sum(r["confidence"] for r in retrieved) / len(retrieved)

    prompt = f"""
You are a strict assistant.
Answer ONLY using the context below.
If the answer is not present, say "NO".

Context:
{context}

Question:
{user_query}

Instructions:
- Give a clear and complete answer
- Do NOT add outside knowledge
- Do NOT use '*'

Final Answer:
"""

    answer = query_llm(prompt)

    return answer, avg_confidence



if __name__ == "__main__":
    print("startedd")
    directory_path = "PATH TO DIRECTORY WHICH HOLDS DATA IN PDFS"

    print("\nLoading PDFs...")
    docs = load_pdfs_from_directory(directory_path)

    print("\nSplitting text...")
    chunks = split_docs(docs)

    print("\nBuilding FAISS index...")
    index, embedder = build_faiss_index(chunks)

    print("RAG_READY", flush=True)

    while True:
        query = sys.stdin.readline().strip()

        if not query:
            continue

        

        answer, confidence = answer_query(
            query,
            index,
            embedder,
            chunks
        )

        
        print(f"{answer}||{confidence}", flush=True)
