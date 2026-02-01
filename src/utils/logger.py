"""
Logging configuration for Credit Risk ML System
"""
import os
import logging
from datetime import datetime
from pathlib import Path


# Create logs directory
LOG_DIR = "logs"
LOG_DIR = Path(LOG_DIR)
LOG_DIR.mkdir(exist_ok=True)

# Create log file with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = LOG_DIR / LOG_FILE

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()  # Also print to console
    ]
)


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the specified name.
    
    Args:
        name: Name of the logger (usually __name__ of the module)
        
    Returns:
        Configured logger instance
    """
    return logging.getLogger(name)