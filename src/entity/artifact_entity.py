"""
Artifact entities for pipeline components outputs
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any


@dataclass
class DataIngestionArtifact:
    """Artifact produced by Data Ingestion stage"""
    merged_data_path: Path
    num_records: int


@dataclass
class DataValidationArtifact:
    """Artifact from data validation"""
    validation_status: bool
    report_file_path: Path
    message: str


@dataclass
class DataTransformationArtifact:
    """Artifact from data transformation"""
    train_data_path: Path
    test_data_path: Path
    transformers_path: Path


@dataclass
class ModelTrainerArtifact:
    """Artifact from model training"""
    model_path: Path
    train_accuracy: float
    test_accuracy: float
    train_f1_score: float
    test_f1_score: float


@dataclass
class ModelEvaluationArtifact:
    """Artifact from model evaluation"""
    metrics_file_path: Path
    is_model_accepted: bool
    model_score: float