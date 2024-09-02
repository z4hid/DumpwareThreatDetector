import os, sys
from src.ThreatDetector.logger import logging
from src.ThreatDetector.exception import CustomException
from src.ThreatDetector.constants import *
from src.ThreatDetector.entity.config_entity import DataValidationConfig
from src.ThreatDetector.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.ThreatDetector.utils import read_yaml 


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact):
        """
        __init__ function of DataValidation class.

        This function is used to initialize the DataValidation class.

        Args:
            data_ingestion_artifact (DataIngestionArtifact): Artifact containing the paths to the train, test, and validation datasets.

        Returns:
            None
        """
        self.data_ingestion_artifact = data_ingestion_artifact
        self._schema_config = read_yaml(SCHEMA_FILE_PATH)
    
    def count_classes(self, path):
        """
        Counts the number of classes in the given dataset.

        Args:
            path (str): Path to the dataset.

        Returns:
            bool: True if the number of classes matches the expected number, False otherwise.
        """
        outcomes = os.listdir(path)
        status = len(outcomes) == len(self._schema_config['classes'])
        return status
    
    def initiate_data_validation(self):
        """
        Initiates the data validation component by counting the number of classes in the train and test datasets.

        Args:
            None

        Returns:
            DataValidationArtifact: Artifact containing the result of the data validation.
        """
        try:
            logging.info("Initiating the data validation component...")
            validation_error_msg=''
            status = self.count_classes(path=self.data_ingestion_artifact.train_file_path)
            if not status:
                validation_error_msg += 'Classes are missing in training data'
            status = self.count_classes(path=self.data_ingestion_artifact.test_file_path)
            if not status:
                validation_error_msg += 'Classes are missing in test data'
            
            validation_status = len(validation_error_msg) == 0
            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status,
            )
            logging.info(f"Data Validation Artifact: [{data_validation_artifact}]") 
            return data_validation_artifact
            
        except Exception as e:
            raise CustomException(e, sys)
