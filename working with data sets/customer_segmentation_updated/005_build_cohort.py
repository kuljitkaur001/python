# src/005_build_cohorts.py
# Generates a customer retention cohort analysis

import pandas as pd
import datetime as dt
from pathlib import Path
import argparse
import logging

# --- Setup basic logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# --- Re-using functions from the first script ---
def load_raw(path: str) -> pd.DataFrame:
    """Loads the raw transaction data from a CSV file."""
    logging.info(f"Loading raw data from: {path}")
    try:
        df = pd.read_csv(path, encoding="ISO-8859-1")
        return df
    except FileNotFoundError:
        logging.error(f"Error: The file was not found at {path}")
        raise

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the raw transaction DataFrame."""
    logging.info("Starting transaction data cleaning...")
    df = df.dropna(subset=["CustomerID"]).copy()
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df = df[~df["InvoiceNo"].str.startswith("C")]
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["InvoiceDate"])
    return df

# --- New Cohort Analysis Functions ---
def get_month(x):
    return dt.datetime(x.year, x.month, 1)

def get_cohort_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the cleaned dataframe to create a cohort retention matrix.
    """
    logging.info("Starting cohort analysis...")
    df['InvoiceMonth'] = df['InvoiceDate'].apply(get_month)
    grouping = df.groupby('CustomerID')['InvoiceMonth']
    df['CohortMonth'] = grouping.transform('min')

    def get_date_int(df, column):
        year = df[column].dt.year
        month = df[column].dt.month
        return year, month

    invoice_year, invoice_month = get_date_int(df, 'InvoiceMonth')
    cohort_year, cohort_month = get_date_int(df, 'CohortMonth')

    years_diff = invoice_year - cohort_year
    months_diff = invoice_month - cohort_month
    df['CohortIndex'] = years_diff * 12 + months_diff + 1

    # Count monthly active customers from each cohort
    cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['CustomerID'].apply(pd.Series.nunique).reset_index()
    cohort_count = cohort_data.pivot_table(index='CohortMonth', columns='CohortIndex', values='CustomerID')

    # Calculate retention rate
    cohort_size = cohort_count.iloc[:, 0]
    retention = cohort_count.divide(cohort_size, axis=0)
    retention.index = retention.index.strftime('%Y-%m')
    
    logging.info("Cohort analysis complete.")
    return retention

def cohort_pipeline(raw_csv_path: str, out_csv_path: str):
    """Orchestrates the full cohort analysis pipeline."""
    logging.info("--- Starting Cohort Analysis Pipeline ---")
    
    df_raw = load_raw(raw_csv_path)
    df_clean = clean_transactions(df_raw)
    cohort_retention = get_cohort_data(df_clean)

    out_path = Path(out_csv_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cohort_retention.to_csv(out_path)

    logging.info(f"Cohort retention data saved to: {out_path} ✅")
    logging.info("--- Cohort Analysis Pipeline Finished ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a cohort analysis from raw transaction data.")
    parser.add_argument("--input", type=str, required=True, help="Path to the raw input CSV file.")
    parser.add_argument("--output", type=str, default="artifacts/cohort_retention.csv", help="Path to save the output cohort CSV file.")
    args = parser.parse_args()

    cohort_pipeline(raw_csv_path=args.input, out_csv_path=args.output)
