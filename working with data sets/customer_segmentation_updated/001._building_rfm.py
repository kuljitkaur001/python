# 01_building_rfm.py
"""
Build RFM features + enrich with simple CLV estimate and cohort info.
Saves:
 - artifacts/rfm.csv            (basic RFM)
 - artifacts/rfm_enriched.csv   (RFM + first/last dates + tenure + avg order + CLV estimates + cohort)
"""

import pandas as pd
import numpy as np  # Added for np.where
from pathlib import Path

# File path (corrected for Windows)
RAW_PATH = Path("C:/Users/hp/OneDrive/python/python/working with data sets/Online_Retail_.csv")
ART = Path("artifacts")
ART.mkdir(exist_ok=True)

def load_raw(file_path: Path) -> pd.DataFrame:
    """Load the raw CSV file with specified encoding."""
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist. Please check the path.")
    # Use ISO-8859-1 encoding to handle special characters
    return pd.read_csv(file_path, encoding='ISO-8859-1')

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    # Keep necessary columns defensively
    keep = ["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"]
    df = df[[c for c in keep if c in df.columns]].copy()
    # Drop missing customers and cancellations and invalid values
    df = df.dropna(subset=["CustomerID"])
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df = df[~df["InvoiceNo"].str.startswith("C")]  # Remove cancellations
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["InvoiceDate"])
    df["Amount"] = df["Quantity"] * df["UnitPrice"]
    df["CustomerID"] = df["CustomerID"].astype(str)
    return df

def compute_rfm(df: pd.DataFrame) -> pd.DataFrame:
    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    rfm = df.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("Amount", "sum"),
        FirstPurchase=("InvoiceDate", "min"),
        LastPurchase=("InvoiceDate", "max")
    ).reset_index()
    return rfm

def enrich_with_clv_and_cohort(rfm: pd.DataFrame) -> pd.DataFrame:
    # Tenure in days / years
    rfm["TenureDays"] = (rfm["LastPurchase"] - rfm["FirstPurchase"]).dt.days.replace(0, 1)
    rfm["TenureYears"] = rfm["TenureDays"] / 365.0

    # Average order value (safety: if frequency==0)
    rfm["AvgOrder"] = (rfm["Monetary"] / rfm["Frequency"]).replace([float("inf"), -float("inf")], 0).fillna(0)

    # Purchases per year (estimated from tenure)
    # Use np.where to handle infinite values row-by-row
    purchases_per_year = rfm["Frequency"] / rfm["TenureYears"]
    rfm["PurchasesPerYear"] = np.where(
        np.isinf(purchases_per_year) | np.isnan(purchases_per_year),
        rfm["Frequency"],
        purchases_per_year
    )

    # Simple CLV estimates:
    #  - est_CLV_1yr: estimated customer value for next 1 year
    #  - est_CLV_tenure: extrapolate based on historical tenure (not a prediction)
    rfm["est_CLV_1yr"] = rfm["AvgOrder"] * rfm["PurchasesPerYear"] * 1.0
    rfm["est_CLV_tenure"] = rfm["AvgOrder"] * rfm["PurchasesPerYear"] * rfm["TenureYears"]

    # Cohort month = first purchase month (YYYY-MM)
    rfm["CohortMonth"] = rfm["FirstPurchase"].dt.to_period("M").astype(str)

    # Round numeric columns for neatness
    rfm[["Recency", "Frequency", "Monetary", "TenureDays", "TenureYears", "AvgOrder", "PurchasesPerYear", "est_CLV_1yr", "est_CLV_tenure"]] = \
        rfm[["Recency", "Frequency", "Monetary", "TenureDays", "TenureYears", "AvgOrder", "PurchasesPerYear", "est_CLV_1yr", "est_CLV_tenure"]].round(2)

    return rfm

def build_all(raw_path=RAW_PATH):
    raw = load_raw(raw_path)
    raw_clean = clean_transactions(raw)
    rfm = compute_rfm(raw_clean)

    # Save basic RFM
    rfm_basic = rfm[["CustomerID", "Recency", "Frequency", "Monetary"]].copy()
    rfm_basic.to_csv(ART / "rfm.csv", index=False)

    # Enriched RFM with CLV & cohort
    rfm_enriched = enrich_with_clv_and_cohort(rfm)
    rfm_enriched.to_csv(ART / "rfm_enriched.csv", index=False)

    print("Saved:", ART / "rfm.csv")
    print("Saved:", ART / "rfm_enriched.csv")
    return rfm_enriched

if __name__ == "__main__":
    build_all()