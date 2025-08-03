from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

"""
Type on the CLI: huggingface-cli login
Copy the token from the .secret file
"""

model = AutoModelForSeq2SeqLM.from_pretrained("artifacts/model_trainer/pegasus-samsum-model")
tokenizer = AutoTokenizer.from_pretrained("artifacts/model_trainer/tokenizer")

# Push to Hub (replace with your username and model name)
model.push_to_hub("Chrisus3/text-summarizer")
tokenizer.push_to_hub("Chrisus3/text-summarizer")