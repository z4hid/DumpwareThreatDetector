import os
import sys
from zipfile import Path, ZipFile
from dataclasses import dataclass
from src.ThreatDetector.constants import *
from datetime import datetime
from from_root import from_root

# Generate a timestamp for file naming
TIMESTAMP: str = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


@dataclass
class DataIngestionConfig:
    """
    Data class for storing configuration parameters related to data ingestion.
    """

    # Path where the data ingestion artifacts are stored
    data_ingestion_artifact_dir: str = os.path.join(
        from_root(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR
    )

    # URL to the zip file containing the training and test data
    zip_data_path: str = (
        'https://drive.google.com/file/d/1r4md2pXWYgib4EFLFHT0rGFVQRiaaLuO/view?usp=sharing'
    )

    # Path to the directory containing the training data
    train_data_path: str = os.path.join(
        data_ingestion_artifact_dir, TRAIN_FOLDER_NAME
    )

    # Path to the directory containing the test data
    test_data_path: str = os.path.join(
        data_ingestion_artifact_dir, TEST_FOLDER_NAME
    )

    # # Path to the directory containing the validation data
    # valid_data_path: str = os.path.join(
    #     data_ingestion_artifact_dir, VALIDATION_FOLDER_NAME
    # )


@dataclass
class DataValidationConfig:
    """
    Data class for storing configuration parameters related to data validation.
    """

    # Path to the schema file
    schema_file_path: str = os.path.join(from_root(), SCHEMA_FILE_PATH)


