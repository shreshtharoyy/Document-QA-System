# DocuMind-QA

DocuMind-QA is a PDF Question Answering system that enables users to upload documents and ask natural language questions about their content. The system retrieves the most relevant document chunks using semantic similarity and extracts answers from the retrieved context.

## Features

* Upload and process PDF documents
* Semantic document retrieval using sentence embeddings
* Context-based question answering
* FastAPI backend for document processing and inference
* Gradio frontend for interactive usage
* Retrieval-based document understanding


---

## Demo

A short demonstration video is available in the `demo` folder.

**Demo Video:** `demo/documind_demo.mp4`

The demo showcases:

* PDF upload and processing
* Semantic document retrieval
* Question answering from uploaded documents
* End-to-end interaction through the web interface


---

## System Architecture

```text
PDF Upload
    ↓
Text Extraction (PyMuPDF)
    ↓
Document Chunking
    ↓
Sentence Embeddings
    ↓
Cosine Similarity Retrieval
    ↓
Relevant Context Selection
    ↓
Question Answering Model
    ↓
Answer
```

---

## Tech Stack

### Backend

* FastAPI
* Python

### Frontend

* Gradio

### NLP & Machine Learning

* Sentence Transformers
* RoBERTa
* scikit-learn

### Document Processing

* PyMuPDF

---

## Models Used

### Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

Used for generating dense vector representations of document chunks and user queries.

### Question Answering Model

```text
deepset/roberta-base-squad2
```

Used to extract answers from the retrieved document context.

---

## Project Structure

```text
DocuMind-QA/
│
├── app.py
├── run_pipeline.py
├── requirements.txt
│
├── frontend/
│   └── app.py
│
├── pipeline/
│   ├── ingest.py
│   ├── encoder.py
│   ├── retriever.py
│   └── generator.py
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd DocuMind-QA
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Backend

```bash
uvicorn app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

```bash
python frontend/app.py
```

---

## Usage

1. Upload a PDF document.
2. Process the document.
3. Ask questions about the uploaded document.
4. Receive answers extracted from the most relevant document context.

---

## Key Concepts

* Semantic Search
* Sentence Embeddings
* Cosine Similarity Retrieval
* Document Question Answering
* Context Retrieval
* Extractive Question Answering

---

## Future Enhancements

* Multi-document support
* Persistent document storage
* Vector database integration
* Conversational document question answering
* Cloud deployment
* User session management
