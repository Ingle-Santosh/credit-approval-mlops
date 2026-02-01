import os
import pandas as pd
import pytest
from pathlib import Path

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact


@pytest.fixture
def data_ingestion_config(tmp_path):
    """
    Temporary ingestion config for testing
    """
    return DataIngestionConfig(
        raw_internal_data_path=Path("data/raw/internal/internal_bank_data.xlsx"),
        raw_external_data_path=Path("data/raw/external/external_cibil_data.xlsx"),
        interim_data_path=tmp_path / "merged_credit_data.csv",
        merge_key="PROSPECTID"
    )


def test_data_ingestion_success(data_ingestion_config):
    """
    Test data ingestion and merge
    """
    ingestion = DataIngestion(config=data_ingestion_config)

    artifact: DataIngestionArtifact = ingestion.initiate_data_ingestion()

    # ---- File existence ----
    assert os.path.exists(artifact.merged_data_path)

    # ---- Content validation ----
    df = pd.read_csv(artifact.merged_data_path)

    assert not df.empty
    assert artifact.num_records == df.shape[0]
    assert "PROSPECTID" in df.columns
