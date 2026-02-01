"""
Configuration entities for pipeline components
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict, Any


@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration for data ingestion component"""
    raw_internal_data_path: Path
    raw_external_data_path: Path
    interim_data_path: Path
    merge_key: str = "PROSPECTID"


@dataclass(frozen=True)
class DataValidationConfig:
    """Configuration for data validation component"""
    root_dir: Path
    merged_data: Path
    schema_file: Path
    status_file: Path
    report_file: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    """Configuration for data transformation component"""
    root_dir: Path
    data_path: Path
    train_data: Path
    test_data: Path
    transformers_path: Path
    test_size: float
    random_state: int
    stratify_column: str


@dataclass(frozen=True)
class ModelTrainerConfig:
    """Configuration for model training component"""
    root_dir: Path
    train_data: Path
    test_data: Path
    transformers_path: Path
    model_path: Path
    model_name: str
    random_state: int
    params: Optional[Dict[str, Any]] = None


@dataclass(frozen=True)
class ModelEvaluationConfig:
    """Configuration for model evaluation component"""
    root_dir: Path
    test_data: Path
    model_path: Path
    transformers_path: Path
    metrics_file: Path
    mlflow_uri: str