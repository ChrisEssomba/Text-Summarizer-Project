


from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.config.configuration import ConfigurationManager


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    #update the pipeline
    def main(self):  
        try: 
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config= model_trainer_config)
            model_trainer_config.train()
        except Exception as e: 
            raise e