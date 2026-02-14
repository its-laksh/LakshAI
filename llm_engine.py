from gpt4all import GPT4All

model = GPT4All("ggml-model.bin")

def generate_response(prompt):
    response = model.generate(prompt)
    return response
