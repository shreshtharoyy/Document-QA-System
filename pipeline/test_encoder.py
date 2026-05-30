from ingest import load_text, chunk_text
from encoder import encode_text

chunks = chunk_text(load_text("sample.pdf"))
for i, chunk in enumerate(chunks, start=1):
    embedding = encode_text(chunk)
    print(f"Chunk {i}: {embedding.shape}\n")