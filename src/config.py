"""
Configurações e Constantes do Projeto
Parkinson's Disease Voice Analysis
"""

from dataclasses import dataclass
from typing import List, Dict
import numpy as np

@dataclass
class ProjectConfig:
    """Configurações globais do projeto"""
    
    # Dados
    DATASET_ID: int = 174  # UCI Repository ID
    RANDOM_STATE: int = 42
    TEST_SIZE: float = 0.2
    CV_FOLDS: int = 5
    
    # Thresholds
    DECISION_THRESHOLD: float = 0.5
    UNCERTAINTY_ZONE: tuple = (0.4, 0.6)
    OVERFITTING_GAP_THRESHOLD: float = 0.15
    
    # Features
    TARGET_COLUMN: str = 'status'
    DROP_COLUMNS: List[str] = None
    
    def __post_init__(self):
        if self.DROP_COLUMNS is None:
            self.DROP_COLUMNS = ['name']
    
    # Métricas de avaliação
    SCORING_METRICS: Dict[str, str] = None
    
    def get_scoring_metrics(self):
        if self.SCORING_METRICS is None:
            self.SCORING_METRICS = {
                'accuracy': 'accuracy',
                'recall': 'recall',
                'f1': 'f1',
                'roc_auc': 'roc_auc'
            }
        return self.SCORING_METRICS
    
    # XGBoost parameters
    XGBOOST_PARAMS: Dict = None
    
    def get_xgboost_params(self):
        if self.XGBOOST_PARAMS is None:
            self.XGBOOST_PARAMS = {
                'random_state': self.RANDOM_STATE,
                'eval_metric': 'logloss',
                'base_score': 0.5
            }
        return self.XGBOOST_PARAMS
    
    # Visualização
    PLOT_STYLE: str = 'seaborn-v0_8-darkgrid'
    FIGURE_DPI: int = 100
    COLOR_PALETTE: str = 'viridis'

@dataclass
class FeatureGroups:
    """Agrupamento de features por categoria biomédica"""
    
    JITTER_FEATURES: List[str] = None
    SHIMMER_FEATURES: List[str] = None
    FREQUENCY_FEATURES: List[str] = None
    NOISE_FEATURES: List[str] = None
    NONLINEAR_FEATURES: List[str] = None
    
    def __post_init__(self):
        self.JITTER_FEATURES = [
            'MDVP:Jitter', 'MDVP:Jitter.1', 'MDVP:RAP', 
            'MDVP:PPQ', 'Jitter:DDP'
        ]
        
        self.SHIMMER_FEATURES = [
            'MDVP:Shimmer', 'MDVP:Shimmer.1', 'Shimmer:APQ3',
            'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA'
        ]
        
        self.FREQUENCY_FEATURES = [
            'MDVP:Fo', 'MDVP:Fhi', 'MDVP:Flo'
        ]
        
        self.NOISE_FEATURES = ['NHR', 'HNR']
        
        self.NONLINEAR_FEATURES = [
            'RPDE', 'D2', 'DFA', 'spread1', 'spread2', 'PPE'
        ]

# Instâncias globais
CONFIG = ProjectConfig()
FEATURE_GROUPS = FeatureGroups()