import os, sys
import joblib
from src.ThreatDetector.logger import logging
from src.ThreatDetector.exception import CustomException
from src.ThreatDetector.constants import *
from src.ThreatDetector.entity.config_entity import *
from src.ThreatDetector.entity.artifact_entity import *
from src.ThreatDetector.entity.custom_model import *
from src.ThreatDetector.utils import *

from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, random_split
import torchvision.transforms as tt 


class ModelTraining:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, model_training_config: ModelTrainingConfig):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.model_training_config = model_training_config
        
    def get_data_loader(self, train_data):
        """
        Method to create PyTorch data loaders from the given dataset.

        Args:
            train_data (Dataset): The dataset to be split into training and validation sets.

        Returns:
            Tuple of two DataLoaders: The first DataLoader is for the training set and the second DataLoader is for the validation set.

        Raises:
            CustomException: If there is an error during the data loader creation process.
        """
        try:
            val_size = int(len(train_data) * 0.2)
            train_size = len(train_data) - val_size
            logging.info("Shuffle and split the training and validation set")
            train_ds, val_ds = random_split(train_data, [train_size, val_size])
            # PyTorch data loaders
            training_dl = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, num_workers=0, pin_memory=True)
            valid_dl = DataLoader(val_ds, batch_size=BATCH_SIZE*2, num_workers=0, pin_memory=True)
            logging.info("Exit get_data_loader method of ModelTraining class")
            return training_dl, valid_dl
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def get_model(self, train_data):
        """
        Method to get the custom PyTorch model.

        Args:
            train_data (Dataset): The dataset containing the number of classes.

        Returns:
            model: The custom PyTorch model.

        Raises:
            CustomException: If there is an error getting the custom model.
        """
        try:
            logging.info("Get the custom model")
            num_classes = len(train_data.classes)
            model = ResNet9(3, num_classes=num_classes)
            return model
        except Exception as e:
            raise CustomException(e, sys)

    def load_to_GPU(self, training_dl, valid_dl, model):
        """
        Loads the model, training data loader and validation data loader to the GPU.

        Args:
            training_dl (DataLoader): The training data loader.
            valid_dl (DataLoader): The validation data loader.
            model (nn.Module): The custom PyTorch model.

        Returns:
            Tuple of three objects: The training data loader, validation data loader, and the custom PyTorch model, all loaded to the GPU.

        Raises:
            CustomException: If there is an error loading the data or model to the GPU.
        """
        try:
            logging.info("Load the model to GPU")
            DEVICE = get_default_device()
            model = to_device(model, DEVICE)
            logging.info("Loading data to GPU")
            training_dl = DeviceDataLoader(training_dl, DEVICE)
            valid_dl = DeviceDataLoader(valid_dl, DEVICE)
            logging.info("Loading data and model to GPU is done")
            return training_dl, valid_dl, model
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def train_model(self, model, train_dl, valid_dl):
        """
        Method to train the model.

        Args:
            model (nn.Module): The custom PyTorch model.
            train_dl (DataLoader): The training data loader.
            valid_dl (DataLoader): The validation data loader.

        Returns:
            Tuple of two objects: The first object is the trained model, and the second object is the result of model training.

        Raises:
            CustomException: If there is an error during the model training process.
        """
        try:
            logging.info("Start training the model")
            fitted_model, result = my_fit_method(
                epochs=EPOCHS,
                lr=LEARNING_RATE,
                model=model,
                train_data_loader=train_dl,
                valid_data_loader=valid_dl,
                optimizer=OPTIMIZER,
                grad_clip=GRAD_CLIP
            )
            grad_clip = GRAD_CLIP
            logging.info("Model Training DONE!")
            return fitted_model, result
        except Exception as e:
            raise CustomException(e, sys)
         
    def initiate_model_training(self):
        """
        Initiates the model training component by performing the following operations:
        1. Create a PyTorch data loader for the training dataset.
        2. Create a PyTorch data loader for the validation dataset.
        3. Load the custom PyTorch model.
        4. Load the model to the GPU.
        5. Train the model using the specified hyperparameters.
        6. Save the trained model to the specified path.
        7. Save the transformer object to the specified path.
        8. Return a ModelTrainingArtifacts object containing the trained model path, result of model training, and transformer object path.

        Raises:
            CustomException: If there is an error during the model training process.
        """
        try:
            logging.info("Initiating the model training component...")
            
            stats = ((0.4301, 0.4574, 0.4537), (0.2482, 0.2467, 0.2807))
            train_transform = tt.Compose([
                tt.Resize(224),
                tt.RandomCrop(224),
                tt.RandomHorizontalFlip(p=0.5),
                tt.ToTensor(),
                tt.Normalize(*stats, inplace=True)
            ])
            
            os.makedirs(self.model_training_config.model_trainer_artifact_dir, exist_ok=True)
            logging.info("Saving transformer object for prediction")
            joblib.dump(train_transform, os.path.join(self.model_training_config.transformer_object_path))
            logging.info("Applying set of transformations on training data")
            train_data = ImageFolder(self.data_ingestion_artifact.train_file_path, transform=train_transform)
            train_dl, val_dl = self.get_data_loader(train_data)
            logging.info("Load the custom model")
            model = self.get_model(train_data)
            torch.cuda.empty_cache()
            logging.info("Load the requiremnets to GPU")
            train_dl, val_dl, model = self.load_to_GPU(train_dl, val_dl, model)
            fitted_model, result = self.train_model(model=model, train_dl=train_dl, valid_dl=val_dl)
            logging.info(f"Saving the model at {self.model_training_config.model_path}")
            torch.save(model.state_dict(), self.model_training_config.model_path)
            
            model_trainer_artifact = ModelTrainingArtifacts(
                model_path=self.model_training_config.model_path,
                result=result,
                transformer_object_path=self.model_training_config.transformer_object_path
            )
            logging.info(f"Model training artifact {model_trainer_artifact}")
            logging.info("Model training completed")
            return model_trainer_artifact

            
        except Exception as e:
            raise CustomException(e, sys)