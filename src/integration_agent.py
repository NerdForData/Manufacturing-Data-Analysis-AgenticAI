import pandas as pd
import numpy as np

def normalize_id_val(v):
    if pd.isna(v):
        return np.nan
    return str(v).strip().lower().replace(" ", "").replace("-", "").replace("_", "")

class IntegrationAgent:
    def __init__(self, mappings: dict):
        self.mappings = mappings

    def unify_direct(self, df_erp, df_cmm, erp_key: str, cmm_key: str):
        erp = df_erp.copy()
        cmm = df_cmm.copy()
        erp['_join_key'] = erp[erp_key].apply(normalize_id_val)
        cmm['_join_key'] = cmm[cmm_key].apply(normalize_id_val)
        merged = pd.merge(cmm, erp, left_on='_join_key', right_on='_join_key', how='left')
        merged.drop(columns=['_join_key'], inplace=True, errors='ignore')
        return merged
