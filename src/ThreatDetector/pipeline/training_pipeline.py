import os, sys
from src.ThreatDetector.exception import CustomException
from src.ThreatDetector.logger import logging
from src.ThreatDetector.components.data_ingestion import DataIngestion
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
        
    