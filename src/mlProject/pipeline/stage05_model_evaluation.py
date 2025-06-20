from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
    
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config = model_evaluation_config)
        model_evaluation_config.prediction()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>Stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        model_evaluation_config = obj.main()
        logger.info(f">>>>>>>>stage {STAGE_NAME} completed<<<<<<<<<\n\nx=============x")

    except Exception as e:
        raise e