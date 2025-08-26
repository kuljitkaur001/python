# src/01_build_rfm.py
# Reproducible RFM feature builder

import pandas as pd
import numpy as np
from pathlib import Path
import datetime as dt

def load_raw(path: str) -> pd.DataFrame:
    # UCI/Kaggle export often needs ISO-8859-1
    df = pd.read_csv(path, encoding="ISO-8859-1")
    # keep only necessary columns (defensive)
    keep = ["InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"]
    df = df[[c for c in keep if c in df.columns]]
    return df

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["CustomerID"]).copy()
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df = df[~df["InvoiceNo"].str.startswith("C")]                # remove cancellations
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]       # keep valid sales only
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["InvoiceDate"])
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    return df

def compute_rfm(df: pd.DataFrame) -> pd.DataFrame:
    reference_date = df["InvoiceDate"].max() + dt.timedelta(days=1)
    rfm = df.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("TotalPrice", "sum"),
    ).reset_index()
    # tidy types
    rfm["CustomerID"] = rfm["CustomerID"].astype(str)
    rfm = rfm.sort_values("CustomerID").reset_index(drop=True)
    return rfm

def build_rfm(raw_csv_path: str, out_csv_path: str) -> pd.DataFrame:
    df_raw = load_raw(raw_csv_path)
    df_clean = clean_transactions(df_raw)
    rfm = compute_rfm(df_clean)

    out_path = Path(out_csv_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rfm.to_csv(out_path, index=False)

    print(f"RFM built ✅  rows={len(rfm)}  ->  {out_path}")
    print(rfm.head())
    return rfm

if __name__ == "__main__":
    # adjust paths if needed
    build_rfm(raw_csv_path="C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\Online_Retail_.csv", out_csv_path="artifacts/rfm.csv")
