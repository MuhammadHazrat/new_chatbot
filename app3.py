# Import generic wrappers
from transformers import AutoModel, AutoTokenizer

# Define the model repo
model_name = "typeform/distilbert-base-uncased-mnli"

# Download pytorch model
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

candidate_labels = ['travel', 'greetings', 'help', 'health']
# Transform input tokens
inputs = tokenizer("Hello world!", return_tensors="pt")

# Model apply
outputs = model(**inputs)

print(outputs)
