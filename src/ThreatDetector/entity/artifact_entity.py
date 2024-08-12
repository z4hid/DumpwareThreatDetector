from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str
    valid_file_path: str
    data_path: str
    
    
@dataclass
class DataValidationArtifact:
    validation_status: bool
    
