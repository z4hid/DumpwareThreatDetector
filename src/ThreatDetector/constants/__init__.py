import os
import torch
from from_root import from_root

ARTIFACTS_DIR: str = 'artifacts'
SOURCE_DIR_NAME: str = 'src'

ZIP_FILE_NAME: str = 'data.zip'
TRAIN_FOLDER_NAME: str = 'train'
TEST_FOLDER_NAME: str = 'test'
VALIDATION_FOLDER_NAME: str = 'valid'

# Data Ingestion related constants
ARTIFACTS_DIR = os.path.join(from_root(), 'artifacts')
BUCKET_NAME = 'dumpware10'
CLOUD_DATA_FOLDER_NAME = 'data.zip'
DATA_INGESTION_ARTIFACTS_DIR = 'DataIngestion'
UNZIP_FOLDER_NAME = 'data/'


# Data validation related constants
SCHEMA_FILE_PATH = os.path.join(from_root(), 'config', 'schema.yaml')

# Model Training related constants
MODEL_TRAINING_ARTIFACTS_DIR: str = 'ModelTraining'
MODEL_NAME: str = 'model.pth'
BATCH_SIZE: int = 32
EPOCHS = 10
LEARNING_RATE = 0.0001
GRAD_CLIP: float = 0.1
WEIGHT_DECAY: float = 1e-4
IN_CHANNELS: int = 3
OPTIMIZER = torch.optim.Adam
NUM_CLASSES: int = 86