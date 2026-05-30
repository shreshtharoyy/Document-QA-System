from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-360M-Instruct")
model = AutoModelForCausalLM.from_pretrained("HuggingFaceTB/SmolLM2-360M-Instruct")

def generate_answer(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=15, do_sample=False, repetition_penalty=1.1)

    # print("Prompt Length:", inputs["input_ids"].shape[1])
    # print("Output Length:", outputs.shape[1])

    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    # print("Generated Tokens:", generated_tokens)

    answer = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    answer = answer.split("Answer:")[-1].strip()

    return answer.strip()

