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


@dataclass
class DataValidationConfig:
    """
    Data class for storing configuration parameters related to data validation.
    """

    # Path to the schema file
    schema_file_path: str = os.path.join(from_root(), SCHEMA_FILE_PATH)


@dataclass
class ModelTrainingConfig:
    model_trainer_artifact_dir = os.path.join(from_root(), ARTIFACTS_DIR, MODEL_TRAINING_ARTIFACTS_DIR)
    model_path: str = os.path.join(model_trainer_artifact_dir, MODEL_NAME)
    transformer_object_path: str = os.path.join(model_trainer_artifact_dir, TRANSFORM_OBJECT_NAME)
    

@dataclass
class ModelEvaluationConfig:
    hf_model_path: str = HF_MODEL_URI
    model_evaluation_artifact_dir = os.path.join(from_root(), ARTIFACTS_DIR, MODEL_EVALUATION_ARTIFACTS_DIR)
    # best_model_dir: str = os.path.join(model_evaluation_artifact_dir, HF_MODEL_DIR_NAME)
    best_model: str = HF_MODEL_NAME
    best_model_path: str = os.path.join(model_evaluation_artifact_dir, best_model)
    
    
@dataclass
class PredictionPipelineConfig:
    hf_model_path: str = HF_MODEL_URI
    prediction_artifact_dir = os.path.join(from_root(), ARTIFACTS_DIR, PREDICTION_PIPLEINE_DIR_NAME)
    model_download_path = os.path.join(prediction_artifact_dir, MODEL_NAME)
    transforms_path = os.path.join(prediction_artifact_dir, TRANSFORM_OBJECT_NAME)
    
