import fitz

def load_text(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def chunk_text(text):
    chunks = text.split("\n")
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return chunks

chunks = chunk_text(load_text("sample.pdf"))
for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i} \n{chunk}\n")
