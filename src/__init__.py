"""
Parkinson's Disease Voice Analysis - ML Module
Authors: Luana Caldas e Elaine Martins da Silva
Institution: FIAP
Professor: Poliana Nascimento Ferreira
"""

__version__ = "1.0.0"
__author__ = "Luana Caldas, Elaine Martins da Silva"

from .config import CONFIG, FEATURE_GROUPS
from .data_loader import DataLoader, load_and_validate_data
from .preprocessing import DataPreprocessor, preprocess_pipeline
from .models import ModelTrainer

__all__ = [
    'CONFIG',
    'FEATURE_GROUPS',
    'DataLoader',
    'load_and_validate_data',
    'DataPreprocessor',
    'preprocess_pipeline',
    'ModelTrainer',
]