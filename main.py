from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


logger.info("Welcome to our app")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<<<")
except Exception as e: 
    logger.exception(e)
    raise