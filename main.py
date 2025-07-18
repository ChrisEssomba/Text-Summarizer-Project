from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidation, DataValidationTrainingPipeline

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


STAGE_NAME = "Data validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<<<")
except Exception as e: 
    logger.exception(e)
    raise