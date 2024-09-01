from src.ThreatDetector.logger import logging
from src.ThreatDetector.pipeline.training_pipeline import TrainPipeline

logging.info("Demo Log Started")

pipepline = TrainPipeline()

pipepline.run_pipeline()

