import pandas as pd
from pathlib import Path
from typing import List
import sys

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import CreditRiskException
from src.utils.logger import logging


INTERNAL_REQUIRED_COLUMNS = {
    "PROSPECTID"
}

EXTERNAL_REQUIRED_COLUMNS = {
    "PROSPECTID",
    "Approved_Flag"
}


class DataIngestion:
    """
    Data Ingestion component for loading and merging credit data.
    """
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        logging.info("Data Ingestion component initialized")

    def _validate_file_exists(self, path: Path):
        """
        Validate that file exists at given path.
        """
        if not path.exists():
            raise CreditRiskException(f"File not found: {path}")

    def _validate_required_columns(self, df: pd.DataFrame, required_columns: List[str], dataset_name: str):
        """
        Validate that required columns exist in DataFrame.
        """
        missing_cols = set(required_columns) - set(df.columns)
        if missing_cols:
            raise CreditRiskException(
                f"Missing columns in {dataset_name}: {missing_cols}"
            )

    def _load_excel(self, path: Path) -> pd.DataFrame:
        """
        Load Excel file into DataFrame.
        """
        logging.info(f"Reading data from: {path}")
        return pd.read_excel(path)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Main method to run the complete data ingestion pipeline.
        """
        try:
            logging.info("Starting data ingestion")

            # Validate files
            logging.info("validating input files")
            self._validate_file_exists(self.config.raw_internal_data_path)
            self._validate_file_exists(self.config.raw_external_data_path)
            logging.info("All input files found")

            # Load data
            logging.info("Loading internal bank data...")
            internal_df = self._load_excel(self.config.raw_internal_data_path)
            logging.info(f"Internal data loaded: {internal_df.shape}")

            logging.info("Loading external CIBIL data...")
            external_df = self._load_excel(self.config.raw_external_data_path)
            logging.info(f"External data loaded: {external_df.shape}")


            # Validate schemas
            logging.info("Validating data schemas...")
            self._validate_required_columns(
                internal_df,
                INTERNAL_REQUIRED_COLUMNS,
                "Internal Bank Data"
            )

            self._validate_required_columns(
                external_df,
                EXTERNAL_REQUIRED_COLUMNS,
                "External CIBIL Data"
            )
            
            logging.info("Schema validation passed")

            # Drop duplicate keys
            logging.info("Checking for duplicate keys...")
            internal_before = len(internal_df)
            external_before = len(external_df)
            
            internal_df = internal_df.drop_duplicates(subset=[self.config.merge_key])
            external_df = external_df.drop_duplicates(subset=[self.config.merge_key])
            
            if len(internal_df) < internal_before:
                logging.warning(
                    f"Removed {internal_before - len(internal_df)} duplicate keys from internal data"
                )
            if len(external_df) < external_before:
                logging.warning(
                    f"Removed {external_before - len(external_df)} duplicate keys from external data"
                )


            # Merge datasets
            logging.info("Merging internal and external datasets")
            merged_df = internal_df.merge(
                external_df,
                on=self.config.merge_key,
                how="inner"
            )
            # Critical target validation after merge
            if "Approved_Flag" not in merged_df.columns:
                raise CreditRiskException(
                    "Target column Approved_Flag missing after merge",
                    sys
                )
            logging.info(f"Merge completed: {merged_df.shape}")
            logging.info(f"Internal records: {len(internal_df):,}")
            logging.info(f"External records: {len(external_df):,}")
            logging.info(f"Merged records: {len(merged_df):,}")
            logging.info(f"Total columns: {len(merged_df.columns)}")

            # Create output directory
            self.config.interim_data_path.parent.mkdir(parents=True, exist_ok=True)

            # Save merged data
            logging.info(f"Saving merged data to: {self.config.interim_data_path}")
            merged_df.to_csv(self.config.interim_data_path, index=False)
            file_size = self.config.interim_data_path.stat().st_size / 1024
            logging.info(
                f"Merged data saved at {self.config.interim_data_path} "
                f"with {merged_df.shape[0]} records "
                f"({file_size:.2f} KB)"
            )


            return DataIngestionArtifact(
                merged_data_path=self.config.interim_data_path,
                num_records=merged_df.shape[0]
            )

        except Exception as e:
            logging.error(f"Error occurred in data ingestion: {str(e)}")
            raise CreditRiskException(e, sys)

if __name__ == "__main__":
    config = DataIngestionConfig(
        raw_internal_data_path=Path("data/raw/internal/internal_bank_data.xlsx"),
        raw_external_data_path=Path("data/raw/external/external_cibil_data.xlsx"),
        interim_data_path=Path("data/interim/merged_credit_data.csv"),
    )

    ingestion = DataIngestion(config)
    artifact = ingestion.initiate_data_ingestion()

    print(artifact)