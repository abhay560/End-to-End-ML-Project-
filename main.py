from pathlib import Path
from mlProject import logger
from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
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


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>Stage {STAGE_NAME} started <<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed <<<<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>>>Stage {STAGE_NAME} started <<<<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed <<<<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e
