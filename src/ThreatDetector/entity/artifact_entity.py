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
    
@dataclass
class ModelTrainingArtifacts:
    model_path: str
    result: dict
    transformer_object_path: str
     
@dataclass
class ModelEvaluationArtifacts:
    hf_model_loss: float
    is_model_accepted: bool
    trained_model_path: str
    hf_model_path: str
    

@dataclass
class ModelPusherArtifcats:
    response: dict
    
@dataclass
class PredictionArtifact:
    predictions: list
