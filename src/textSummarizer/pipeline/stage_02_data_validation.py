from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.constants import *
from textSummarizer.entity import (DataIngestionConfig)
from textSummarizer.utils.common import read_yaml, create_directories


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    #update the pipeline
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()

    