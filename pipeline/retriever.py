from sklearn.metrics.pairwise import cosine_similarity

def retrieve_best_chunk(question_embedding, chunk_embeddings):
    scores = []

    for embedding in chunk_embeddings:
        score = cosine_similarity(question_embedding.reshape(1, -1), embedding.reshape(1, -1))[0][0]
        scores.append(score)
        best_index = scores.index(max(scores))
    return best_index, scores
    


