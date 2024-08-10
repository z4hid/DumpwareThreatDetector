import os
import sys
import zipfile
import gdown

from src.ThreatDetector.logger import logging
from src.ThreatDetector.exception import CustomException
from src.ThreatDetector.entity.config_entity import DataIngestionConfig
from src.ThreatDetector.entity.artifact_entity import DataIngestionArtifact

from src.ThreatDetector.constants import *

import shutil


class DataIngestion:
    """
    Class to handle data ingestion process.
    """

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        """
        Initialize DataIngestion class with data ingestion configuration.

        Args:
            data_ingestion_config (DataIngestionConfig): Data ingestion configuration.
        """
        try:
            # Assign the provided data ingestion configuration to the instance variable
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            # If an exception occurs, raise an AppException with the given exception and sys
            raise CustomException(e, sys)
    
    
    def download_data(self) -> str:
        """
        Downloads data from the specified URL and saves it as a zip file.

        Returns:
            str: Path to the downloaded zip file.
        """
        try:
            # Get the URL and download directory from the configuration
            url = self.data_ingestion_config.zip_data_path
            download_dir = self.data_ingestion_config.data_ingestion_artifact_dir

            # Create the download directory if it doesn't exist
            os.makedirs(download_dir, exist_ok=True)
            
            # Set the name of the zip file
            data_file_name = 'data.zip'
            # Construct the path to the zip file
            zip_file_path = os.path.join(download_dir, data_file_name)

            # Check if the file already exists
            if os.path.exists(zip_file_path):
                # If the file exists, log a message and return the path to the file
                logging.info(f"File already exists at : [{zip_file_path}]. Skipping download.")
                return zip_file_path
            
            # Log the download operation
            logging.info(f"Downloading file from : [{url}] into : [{zip_file_path}]")
            
            # Extract the file ID from the URL
            file_id = url.split('/')[-2]
            # Construct the prefix for the download URL
            prefix = f'https://drive.google.com/uc?export=download&id='
            # Download the file using gdown
            gdown.download(prefix + file_id, zip_file_path, quiet=False)
            # Log the successful download
            logging.info(f"File : [{zip_file_path}] has been downloaded successfully.")
            # Return the path to the downloaded zip file
            return zip_file_path

        except Exception as e:
            # If an exception occurs, raise an AppException with the given exception and sys
            raise CustomException(e, sys)
        
    
    def extract_zip_file(self, zip_file_path: str) -> DataIngestionArtifact:
        """
        Extracts the contents of the specified zip file to the specified directory.

        Args:
            zip_file_path (str): Path to the zip file.

        Returns:
            DataIngestionArtifact: Artifact containing the paths to the train, test, and validation datasets.
        """
        try:
            # Get the paths for train, test, and validation datasets from the configuration
            train_data_path = self.data_ingestion_config.train_data_path
            test_data_path = self.data_ingestion_config.test_data_path
            valid_data_path = self.data_ingestion_config.valid_data_path

            # Create the directories if they don't exist
            os.makedirs(train_data_path, exist_ok=True)
            os.makedirs(test_data_path, exist_ok=True)
            os.makedirs(valid_data_path, exist_ok=True)

            # Use the correct attribute for the extraction directory
            extraction_path = self.data_ingestion_config.data_ingestion_artifact_dir

            # Open the zip file for reading
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # Extract all files from the zip file
                zip_ref.extractall(extraction_path)
                logging.info(f"Extracted all files to {extraction_path}")

            # Create a DataIngestionArtifact with the paths to the train, test, and validation datasets
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=train_data_path,
                test_file_path=test_data_path,
                valid_file_path=valid_data_path,
                data_path=extraction_path
            )

            # Log the successful extraction
            logging.info(f"Data has been extracted successfully to {extraction_path}")
            # Return the DataIngestionArtifact
            return data_ingestion_artifact

        except Exception as e:
            # If an exception occurs, raise an AppException with the given exception and sys
            raise CustomException(e, sys)

        
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiates the data ingestion process by downloading and extracting the data.

        Returns:
            DataIngestionArtifact: Artifact containing the paths to the train, test, and validation datasets.
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        try:
            # Download the data and get the path to the downloaded zip file
            zip_file_path = self.download_data()
            # Extract the zip file and get the DataIngestionArtifact
            data_ingestion_artifact = self.extract_zip_file(zip_file_path=zip_file_path)
            logging.info("Exited initiate_data_ingestion method of DataIngestion class")
            logging.info(f"Data Ingestion Artifact: [{data_ingestion_artifact}]")
            # Return the DataIngestionArtifact
            return data_ingestion_artifact
        
        except Exception as e:
            # If an exception occurs, raise an AppException with the given exception and sys
            raise CustomException(e, sys)
