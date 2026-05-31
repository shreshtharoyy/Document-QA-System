from sklearn.metrics.pairwise import cosine_similarity

def retrieve_best_chunks(question_embedding, chunk_embeddings, top_k=5):

    scores = []
    for embedding in chunk_embeddings:
        score = cosine_similarity(question_embedding.reshape(1, -1), embedding.reshape(1, -1))[0][0]
        scores.append(score)

    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]

    return top_indices, scores
