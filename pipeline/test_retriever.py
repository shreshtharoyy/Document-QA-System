from ingest import load_text, chunk_text
from encoder import encode_text
from retriever import retrieve_best_chunk

chunks = chunk_text(load_text("sample.pdf"))
chunk_embeddings = []

for chunk in chunks:
    chunk_embeddings.append(encode_text(chunk))

question = "When was the Eiffel Tower built?"
question_embedding = encode_text(question)

best_index, scores = retrieve_best_chunk(question_embedding, chunk_embeddings)

print(f"Scores: {scores} Best Chunk:")
print(chunks[best_index])
