import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from run_pipeline import process_document, answer_question
from pydantic import BaseModel

app = FastAPI()

chunks = None
chunk_embeddings = None

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "message": "DocuMind-QA API is running"
    }

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global chunks, chunk_embeddings

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    save_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        with open(save_path, "wb") as pdf_file:
            content = await file.read()
            pdf_file.write(content)

        chunks, chunk_embeddings = process_document(save_path)

        return {
            "message": "PDF processed successfully",
            "filename": file.filename,
            "chunks": len(chunks)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {str(e)}"
        )

    finally:
        if os.path.exists(save_path):
            os.remove(save_path)

@app.post("/ask")
def ask_question(request: QuestionRequest):
    if chunks is None or chunk_embeddings is None:
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF first using /upload endpoint."
        )

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        answer = answer_question(
            request.question,
            chunks,
            chunk_embeddings
        )

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate answer: {str(e)}"
        )