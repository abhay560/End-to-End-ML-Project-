import os
from pathlib import Path
from mlProject import logger
from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd 

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config = data_transformation_config)
                    data_transformation.train_test_splitting()

                else:
                    raise Exception("Your Data Schema is not valid")
        except Exception as e:
            print(e)