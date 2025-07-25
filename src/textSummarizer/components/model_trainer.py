import os
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch

from textSummarizer.entity import ModelTrainerConfig

class ModelTrainer: 
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        dataset_samsum = load_from_disk(self.config.data_path)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)


        # Define training arguments using config values (from YAML)
        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,  # or add eval batch param separately
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
           # evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=int(self.config.save_steps),  # just in case it's stored as float like 1e6
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )

        # Define the Trainer (you might need to adapt this to include tokenization logic)
        trainer = Trainer(
            model=model_pegasus,
            args=training_args,
            tokenizer = tokenizer, 
            data_collator= seq2seq_data_collator,
            train_dataset=dataset_samsum["test"],
            eval_dataset=dataset_samsum["validation"],
        )

        # Launch training
        trainer.train()
        
        #Save model$
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        
        #Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
