import os, sys
from src.ThreatDetector.exception import CustomException
from src.ThreatDetector.logger import logging
from src.ThreatDetector.components.data_ingestion import DataIngestion
from src.ThreatDetector.components.data_validation import DataValidation
from src.ThreatDetector.entity.config_entity import DataIngestionConfig
from src.ThreatDetector.entity.artifact_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact):
        try:
            logging.info("Entered the start_data_validation method of TrainingPipeline class")
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Exited the start_data_validation method of TrainingPipeline class")
            return data_validation_artifact
        except Exception as e:
            raise CustomException(e, sys)
        
    def run_pipeline(self):
        try:
            logging.info('========== Training Pipeline Started ==========')
            data_ingestion_artifact = self.start_data_ingestion()   
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
            print(data_validation_artifact)
        except Exception as e:
            raise CustomException(e, sys)
    