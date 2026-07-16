# 🚗 Motor Laws Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that answers questions about the Indian Motor Vehicles Act and can optionally analyze an uploaded challan (traffic violation) PDF.

The chatbot retrieves relevant legal information from the Motor Vehicles Act and combines it with the uploaded challan (if provided) to generate accurate, context-aware responses.

---

## ✨ Features

- 📖 Ask questions about the Indian Motor Vehicles Act
- 📄 Upload a challan PDF for document-specific queries
- 🔍 Retrieval-Augmented Generation (RAG)
- 💬 Multi-turn conversation support
- 🧠 Context-aware question rewriting
- 📚 Uses semantic search with sentence-transformer embeddings
- ⚖️ Answers only from retrieved legal context (reduces hallucinations)
- 🖥️ Simple Streamlit interface

---

## 🏗️ Project Architecture

```
                User Question
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
        Question Rewriting (LLM)
                      │
                      ▼
          Chroma Vector Database
                      │
          Semantic Similarity Search
                      │
                      ▼
         Relevant Legal Chunks Retrieved
                      │
                      ▼
          Prompt + Retrieved Context
                      │
                      ▼
                 Groq LLM
                      │
                      ▼
              Final Legal Answer
```

---

## 📂 Project Structure

```
Motor-Laws-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── motor_laws.pdf
│
├── src/
│   ├── config.py
│   ├── ingestion.py
│   ├── rag_chain.py
│   ├── text_splitter.py
│   └── vector_store.py
│
└── README.md
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### LLM

- Groq API
- Llama 3.1 8B Instant

### Embeddings

- sentence-transformers/all-MiniLM-L6-v2

### Vector Database

- ChromaDB

### Framework

- LangChain

### Document Processing

- PyPDFLoader

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/motor-laws-chatbot.git

cd motor-laws-chatbot
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Create `.env`

```env
GROQ_API_KEY=your_api_key_here
```

---

### Run the application

```bash
streamlit run app.py
```

---

## 💬 Example Questions

### Motor Laws

- What documents should a driver carry while driving?
- What is the penalty for driving without insurance?
- Explain Section 185.
- What are the penalties for overspeeding?
- What is the fine for driving without a licence?

---

### Challan-based Questions

After uploading a challan:

- Why was this challan issued?
- What sections have been violated?
- What is the total penalty?
- Explain all offences mentioned.
- Is this offence compoundable?

---

## 🧠 How It Works

1. Loads the Motor Vehicles Act PDF.
2. Splits documents into semantic chunks.
3. Converts chunks into embeddings.
4. Stores embeddings in ChromaDB.
5. Retrieves the most relevant chunks using semantic similarity.
6. Rewrites follow-up questions into standalone questions.
7. Sends retrieved context to Groq's Llama model.
8. Generates answers strictly based on retrieved legal information.

---

## 📦 Libraries Used

- streamlit
- langchain
- langchain-community
- langchain-groq
- langchain-huggingface
- chromadb
- sentence-transformers
- pypdf
- python-dotenv

---

## 🎯 Future Improvements

- Citation of legal sections
- Source highlighting
- Hybrid search (BM25 + Vector Search)
- Conversation memory persistence
- Multiple legal document support
- OCR support for scanned challans
- Deploy on Render or Streamlit Community Cloud

---


## ⭐ If you found this project useful

Give this repository a ⭐ on GitHub.