from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def encode_text(text):
    embedding = model.encode(text)

    return embedding