import os
import sys
from zipfile import Path, ZipFile
from dataclasses import dataclass
from src.ThreatDetector.constants import *
from datetime import datetime
from from_root import from_root

TIMESTAMP: str = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

@dataclass
class DataIngestionConfig:
    data_ingestion_artifact_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
    # zip_data_path: str = os.path.join(data_ingestion_artifact_dir, ZIP_FILE_NAME) # CLOUD_DATA_FOLDER_NAME
    zip_data_path: str = 'https://drive.google.com/file/d/1-xFGicUDjIjeh3EdMbESzOYMywAOyotW/view'
    train_data_path: str = os.path.join(data_ingestion_artifact_dir, TRAIN_FOLDER_NAME)
    test_data_path: str = os.path.join(data_ingestion_artifact_dir, TEST_FOLDER_NAME)
    valid_data_path: str = os.path.join(data_ingestion_artifact_dir, VALIDATION_FOLDER_NAME)
    
    
