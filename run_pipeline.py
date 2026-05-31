from pipeline.ingest import load_text, chunk_text
from pipeline.encoder import encode_text
from pipeline.retriever import retrieve_best_chunks
from pipeline.generator import generate_answer

def process_document(pdf_path):
    pdf_text = load_text(pdf_path)
    chunks = chunk_text(pdf_text)

    chunk_embeddings = []
    for chunk in chunks:
        chunk_embeddings.append(encode_text(chunk))

    return chunks, chunk_embeddings

def answer_question(question, chunks, chunk_embeddings):
    question_embedding = encode_text(question)
    top_indices, scores = retrieve_best_chunks(question_embedding, chunk_embeddings)

    best_score = max(scores)
    THRESHOLD = 0.30

    if best_score < THRESHOLD:
        return "Answer not found in document."

    retrieved_chunks = [chunks[i] for i in top_indices]
    context = "\n".join(retrieved_chunks)

    # Debug prints — baad mein delete kar dena
    print(f"Total chunks: {len(chunks)}")
    print(f"Best score: {best_score}")
    print(f"Retrieved context:\n{context}")

    return generate_answer(context, question)

if __name__ == "__main__":
    chunks, chunk_embeddings = process_document("rag_test_document.pdf")
    question = input("Ask a question: ")
    answer = answer_question(question, chunks, chunk_embeddings)
    print("\nAnswer:")
    print(answer)