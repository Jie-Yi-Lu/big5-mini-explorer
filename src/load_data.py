import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file and return a DataFrame."""
    raise NotImplementedError


def load_clean_data(path: str) -> pd.DataFrame:
    # --- Step 1: Load ---
    # Defence: explicit encoding; errors='replace' avoids crash on bad bytes
    df = pd.read_csv(path, sep="\t", encoding="utf-8", encoding_errors="replace")
    total = len(df)

    # Defence: confirm separator worked — expect many columns, not just 1
    assert df.shape[1] > 2, f"Separator may be wrong — only {df.shape[1]} column(s) found"

    # --- Step 2: Inspect dtypes ---
    # Defence: coerce non-numeric values to NaN instead of raising
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["gender"] = pd.to_numeric(df["gender"], errors="coerce")

    # --- Step 3: Filter age ---
    df = df[(df["age"] >= 13) & (df["age"] <= 80)]

    # --- Step 4: Filter gender (drop unstated = 0) ---
    df = df[df["gender"] != 0]

    kept = len(df)
    lost_pct = (total - kept) / total * 100
    print(f"Rows loaded  : {total}")
    print(f"Rows kept    : {kept}")
    print(f"Rows dropped : {total - kept}  ({lost_pct:.1f}%)")

    return df.reset_index(drop=True)
