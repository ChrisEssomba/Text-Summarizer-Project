from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output
    
        """
        from pathlib import Path
from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    



    def predict(self, text):
        # Get the directory where your script lives
        SCRIPT_DIR = Path(__file__).parent.absolute()
        # Resolve paths relative to script location
        tokenizer_path = SCRIPT_DIR / self.config.tokenizer_path
        model_path = SCRIPT_DIR / self.config.model_path
        print("Using tokenizer from:", tokenizer_path)
        
        # Force local loading (avoid Hugging Face Hub)
        tokenizer = AutoTokenizer.from_pretrained(
            str(tokenizer_path),
            local_files_only=True  # ← Critical for deployment!
        )
  
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
        pipe = pipeline(
            "summarization",
            model=str(model_path),
            tokenizer=tokenizer
        )

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)
        return output
        """