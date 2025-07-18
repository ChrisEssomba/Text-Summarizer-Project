from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.constants import *
from textSummarizer.entity import (DataIngestionConfig)
from textSummarizer.utils.common import read_yaml, create_directories


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    #update the pipeline
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_configuration = DataIngestion(config=data_ingestion_config)
        data_configuration.download_file()
        data_configuration.extract_zip_file()

    