from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self, text):
        # Convert paths to absolute paths to ensure filesystem recognition
        tokenizer_path = Path(self.config.tokenizer_path).absolute()
        model_path = Path(self.config.model_path).absolute()
        
        # Verify paths exist
        if not tokenizer_path.exists():
            raise FileNotFoundError(f"Tokenizer path not found: {tokenizer_path}")
        if not model_path.exists():
            raise FileNotFoundError(f"Model path not found: {model_path}")
        
        # Load tokenizer and model from LOCAL PATHS
        tokenizer = AutoTokenizer.from_pretrained(str(tokenizer_path))
        
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