from mlProject import logger
from mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

logger.info("Welcome to our custom log")

STAGE_NAME = "Data Validation Start"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e
