import sys
from car_price.configuration.s3_operations import S3Operation
from car_price.entity.artifacts_entity import (
    DataTransformationArtifacts,
    ModelPusherArtifacts,
    ModelTrainerArtifacts,
)
from car_price.entity.config_entity import ModelPusherConfig
from car_price.exception import CarException
import logging

# initializing logger
logger = logging.getLogger(__name__)


class ModelPusher:
    def __init__(
        self,
        model_pusher_config: ModelPusherConfig,
        model_trainer_artifacts: ModelTrainerArtifacts,
        data_transformation_artifacts: DataTransformationArtifacts,
        s3: S3Operation,
    ):

        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifacts = model_trainer_artifacts
        self.data_transformation_artifacts = data_transformation_artifacts
        self.s3 = s3

    # this is method is used to initiate model pusher
    def initiate_model_pusher(self) -> ModelPusherArtifacts:

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher. 
        
        Output      :    Model pusher artifact 
        """
        logger.info("Entered initiate_model_pusher method of ModelTrainer class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                self.model_trainer_artifacts.trained_model_file_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False,
            )
            logger.info("Uploaded best model to s3 bucket")
            logger.info("Exited initiate_model_pusher method of ModelTrainer class")

            # Saving the model pusher artifacts
            model_pusher_artifact = ModelPusherArtifacts(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH,
            )

            return model_pusher_artifact

        except Exception as e:
            raise CarException(e, sys) from e
