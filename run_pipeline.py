from pipeline.ingest import load_text, chunk_text
from pipeline.encoder import encode_text
from pipeline.retriever import retrieve_best_chunk
from pipeline.generator import generate_answer

def process_document(pdf_path):
    pdf_text = load_text(pdf_path)
    chunks = chunk_text(pdf_text)

    chunk_embeddings = []

    for chunk in chunks:
        chunk_embeddings.append(
            encode_text(chunk)
        )

    return chunks, chunk_embeddings

def answer_question(question, chunks, chunk_embeddings):

    question_embedding = encode_text(question)

    best_index, scores = retrieve_best_chunk(
        question_embedding,
        chunk_embeddings
    )

    best_score = max(scores)

    THRESHOLD = 0.50

    if best_score < THRESHOLD:
        return "Answer not found in document."

    else:
        best_chunk = chunks[best_index]

        prompt = f"""
    You are a helpful question-answering assistant.

    Answer the question ONLY using the provided context.

    If the answer is not present in the context, say:
    "I could not find the answer in the document."

    Context:
    {best_chunk}

    Question:
    {question}

    Answer:
    """

        answer = generate_answer(prompt)
        return answer
    
if __name__ == "__main__":

    chunks, chunk_embeddings = process_document("sample.pdf")

    question = input("Ask a question: ")

    answer = answer_question(
        question,
        chunks,
        chunk_embeddings
    )

    print("\nAnswer:")
    print(answer)