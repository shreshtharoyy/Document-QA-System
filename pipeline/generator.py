from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

def generate_answer(context, question):
    inputs = tokenizer(
        question,
        context,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

    start_index = torch.argmax(outputs.start_logits)
    end_index = torch.argmax(outputs.end_logits) + 1

    tokens = inputs["input_ids"][0][start_index:end_index]
    answer = tokenizer.decode(tokens, skip_special_tokens=True)

    # Confidence check
    start_score = torch.max(outputs.start_logits).item()
    if start_score < 2.0:
        return "I could not find the answer in the document."

    return answer.strip()