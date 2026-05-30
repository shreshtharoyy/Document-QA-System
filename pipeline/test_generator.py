from generator import generate_answer

prompt = """
You are a helpful question-answering assistant.

Use only the provided context to answer the question.

Context:
The Eiffel Tower was completed in 1889.

Question:
When was the Eiffel Tower built?

Answer:
"""

answer = generate_answer(prompt)
print(f"Generated Answer: {answer}")