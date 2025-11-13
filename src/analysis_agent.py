import pandas as pd
from sklearn.ensemble import IsolationForest
from scipy import stats
import numpy as np

class AnalysisAgent:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def pass_fail_summary(self, pass_col: str = 'pass_flag'):
        if pass_col not in self.df.columns:
            return {}
        total = len(self.df)
        passed = int(self.df[pass_col].sum())
        failed = int(((self.df[pass_col]==False)).sum())
        return {'total': total, 'passed': passed, 'failed': failed}

    def defects_by_lot(self, lot_col: str = 'lot_id', pass_col: str = 'pass_flag'):
        if lot_col not in self.df.columns or pass_col not in self.df.columns:
            return pd.DataFrame()
        df = self.df[self.df[pass_col]==False]
        return df.groupby(lot_col).size().reset_index(name='num_defects').sort_values('num_defects', ascending=False)

    def anomaly_detection_iforest(self, feature_cols: list, contamination: float = 0.02):
        df = self.df.copy()
        if not feature_cols:
            return df
        X = df[feature_cols].fillna(0.0)
        try:
            clf = IsolationForest(contamination=contamination, random_state=42)
            preds = clf.fit_predict(X)
            df['anomaly_iforest'] = preds == -1
        except Exception:
            df['anomaly_iforest'] = False
        return df
