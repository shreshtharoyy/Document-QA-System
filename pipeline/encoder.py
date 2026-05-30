from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

def encode_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :]

    return cls_embedding