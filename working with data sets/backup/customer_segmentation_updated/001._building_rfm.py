# src/01_build_rfm.py
# Enhanced, reproducible RFM feature builder

import pandas as pd
import datetime as dt
from pathlib import Path
import argparse
import logging

# --- Setup basic logging ---
# This is more professional than print() for tracking script execution.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler() # Outputs logs to the console
    ]
)

def load_raw(path: str) -> pd.DataFrame:
    """
    Loads the raw transaction data from a CSV file.

    Args:
        path (str): The file path to the raw CSV data.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.
    
    Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        ValueError: If essential columns are missing from the CSV.
    """
    logging.info(f"Attempting to load raw data from: {path}")
    try:
        # UCI/Kaggle export often needs this specific encoding
        df = pd.read_csv(path, encoding="ISO-8859-1")
        logging.info("Raw data loaded successfully.")
    except FileNotFoundError:
        logging.error(f"Error: The file was not found at {path}")
        raise

    # Defensively check for required columns
    required_cols = ["InvoiceNo", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID"]
    if not all(col in df.columns for col in required_cols):
        logging.error("One or more required columns are missing from the CSV.")
        raise ValueError(f"CSV must contain the following columns: {required_cols}")
        
    return df

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the raw transaction DataFrame by handling missing values,
    removing cancelled orders, and filtering out invalid data points.

    Args:
        df (pd.DataFrame): The raw transaction DataFrame.

    Returns:
        pd.DataFrame: A cleaned DataFrame ready for RFM calculation.
    """
    logging.info("Starting transaction data cleaning...")
    
    # Drop rows where CustomerID is null, as they are not useful for segmentation
    df = df.dropna(subset=["CustomerID"]).copy()
    
    # Ensure InvoiceNo is a string to handle potential mixed types
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    
    # Remove cancellation invoices (often marked with a 'C')
    df = df[~df["InvoiceNo"].str.startswith("C")]
    
    # Remove rows with non-positive quantity or unit price, as they are not valid sales
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    
    # Convert InvoiceDate to datetime objects, coercing errors
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["InvoiceDate"]) # Drop rows where date conversion failed
    
    # Calculate total price for each transaction
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    
    logging.info(f"Cleaning complete. Shape of cleaned data: {df.shape}")
    return df

def compute_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes Recency, Frequency, and Monetary (RFM) metrics for each customer.

    Args:
        df (pd.DataFrame): The cleaned transaction DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with CustomerID and their RFM values.
    """
    logging.info("Computing RFM features...")
    
    # Set a reference date for recency calculation (one day after the last transaction)
    reference_date = df["InvoiceDate"].max() + dt.timedelta(days=1)
    
    rfm = df.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days), 
        Frequency=("InvoiceNo", "nunique"), # Count unique invoices for frequency
        Monetary=("TotalPrice", "sum"),
    ).reset_index()
    
    # Ensure CustomerID is a string for consistency
    rfm["CustomerID"] = rfm["CustomerID"].astype(str)
    rfm = rfm.sort_values("CustomerID").reset_index(drop=True)
    
    logging.info("RFM computation complete.")
    return rfm

def build_rfm_pipeline(raw_csv_path: str, out_csv_path: str):
    """
    Orchestrates the full pipeline: load, clean, compute RFM, and save.

    Args:
        raw_csv_path (str): Path to the input raw data file.
        out_csv_path (str): Path to save the output RFM CSV file.
    """
    logging.info("--- Starting RFM Build Pipeline ---")
    
    df_raw = load_raw(raw_csv_path)
    df_clean = clean_transactions(df_raw)
    rfm_features = compute_rfm(df_clean)

    # Ensure the output directory exists
    out_path = Path(out_csv_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save the final RFM features to a CSV
    rfm_features.to_csv(out_path, index=False)

    logging.info(f"RFM features built successfully ✅")
    logging.info(f"Total customers processed: {len(rfm_features)}")
    logging.info(f"Output saved to: {out_path}")
    logging.info("--- RFM Build Pipeline Finished ---")


if __name__ == "__main__":
    # --- Command-Line Interface ---
    # This makes the script reusable and removes hardcoded paths.
    # You can now run it from the terminal like this:
    # python 01_building_rfm.py --input "path/to/your/data.csv" --output "artifacts/rfm.csv"
    
    parser = argparse.ArgumentParser(description="Build RFM features from raw transaction data.")
    parser.add_argument(
        "--input", 
        type=str, 
        required=True, 
        help="Path to the raw input CSV file."
    )
    parser.add_argument(
        "--output", 
        type=str, 
        default="artifacts/rfm.csv", 
        help="Path to save the output RFM CSV file."
    )
    args = parser.parse_args()

    build_rfm_pipeline(raw_csv_path=args.input, out_csv_path=args.output)
