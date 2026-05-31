from fastapi import FastAPI, UploadFile, File
from run_pipeline import process_document

app = FastAPI()
chunks = None
chunk_embeddings = None

@app.get("/")
def home():
    return {
        "message": "DocuMind-QA API is running"
    }

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    global chunks
    global chunk_embeddings

    with open(file.filename, "wb") as pdf_file:
        content = await file.read()
        pdf_file.write(content)

    chunks, chunk_embeddings = process_document(
        file.filename
    )

    return {
        "message": "PDF processed successfully",
        "chunks": len(chunks)
    }
    