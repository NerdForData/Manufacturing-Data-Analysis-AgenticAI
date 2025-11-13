import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, low_memory=False)

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip().replace({'nan': pd.NA})
    return df
