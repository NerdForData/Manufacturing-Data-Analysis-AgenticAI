import re
def normalize_column(colname: str) -> str:
    return re.sub(r'[^a-z0-9]', '_', colname.lower())
