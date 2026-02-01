"""
Custom Exception Handler for Credit Approval ML System
"""
import sys
from typing import Optional


class CreditRiskException(Exception):
    """
    Custom exception class for Credit Risk ML system.
    Provides detailed error messages with file name and line number.
    """
    
    def __init__(self, error_message, error_detail: Optional[sys] = None):
        """
        Initialize custom exception.
        
        Args:
            error_message: The error message
            error_detail: System error details
        """
        super().__init__(str(error_message))
        self.error_message = self._get_detailed_error_message(
            str(error_message), error_detail
        )
    
    @staticmethod
    def _get_detailed_error_message(error_message: str, error_detail: Optional[sys]) -> str:
        """
        Create detailed error message with file name and line number.
        
        Args:
            error_message: Original error message
            error_detail: System error details
            
        Returns:
            Formatted error message with context
        """
        if error_detail is None:
            return error_message
            
        _, _, exc_tb = error_detail.exc_info()
        
        if exc_tb is None:
            return error_message
        
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        
        error_message = (
            f"Error occurred in script: [{file_name}] "
            f"at line number: [{line_number}] "
            f"error message: [{error_message}]"
        )
        
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.error_message}')"
