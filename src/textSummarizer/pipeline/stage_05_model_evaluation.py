


from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.config.configuration import ConfigurationManager


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    #update the pipeline
    def main(self):  
        try: 
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config= model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e: 
            raise e