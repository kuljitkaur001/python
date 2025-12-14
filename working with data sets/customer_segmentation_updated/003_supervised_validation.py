# src/03_supervised_validation.py
# Professional, reproducible pipeline for supervised model validation

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from pathlib import Path
import argparse
import logging

# --- Setup basic logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

def load_labeled_data(path: str) -> pd.DataFrame:
    """
    Loads the customer dataset which includes ground-truth labels.

    Args:
        path (str): Path to the labeled CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    logging.info(f"Loading labeled data from {path}...")
    try:
        df = pd.read_csv(path)
        # Basic validation
        if "segments" not in df.columns:
            raise ValueError("Input CSV must contain a 'segments' column for labels.")
        logging.info("Labeled data loaded successfully.")
        return df
    except FileNotFoundError:
        logging.error(f"Error: Labeled data file not found at {path}.")
        raise

def generate_validation_artifacts(y_test, y_pred, le: LabelEncoder, out_dir: str):
    """
    Generates and saves the classification report and confusion matrix plot.

    Args:
        y_test: True labels from the test set.
        y_pred: Predicted labels from the model.
        le (LabelEncoder): The fitted label encoder to get class names.
        out_dir (str): Directory to save the artifacts.
    """
    report_path = Path(out_dir) / "classification_report.txt"
    cm_plot_path = Path(out_dir) / "confusion_matrix.png"

    # --- Generate and Save Classification Report ---
    logging.info("Generating classification report...")
    report = classification_report(y_test, y_pred, target_names=le.classes_)
    with open(report_path, "w") as f:
        f.write(report)
    logging.info(f"Classification report saved to {report_path}")
    print("\n" + report) # Also print to console for immediate feedback

    # --- Generate and Save Confusion Matrix Plot ---
    logging.info("Generating confusion matrix plot...")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=le.classes_, yticklabels=le.classes_)
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix")
    plt.savefig(cm_plot_path)
    plt.close()
    logging.info(f"Confusion matrix plot saved to {cm_plot_path}")

def validation_pipeline(input_path: str, artifacts_dir: str, label_col: str):
    """
    Orchestrates the full supervised validation pipeline.

    Args:
        input_path (str): Path to the labeled input CSV.
        artifacts_dir (str): Directory to save all output artifacts.
        label_col (str): The name of the column containing the labels.
    """
    logging.info("--- Starting Supervised Validation Pipeline ---")
    
    # --- Data Preparation ---
    df = load_labeled_data(input_path)
    X = df[["Recency", "Frequency", "Monetary"]]
    y = df[label_col]

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # --- Model Training ---
    logging.info("Training Logistic Regression classifier...")
    clf = LogisticRegression(max_iter=1000, random_state=42)
    clf.fit(X_train_scaled, y_train)
    logging.info("Classifier training complete.")

    # --- Evaluation ---
    y_pred = clf.predict(X_test_scaled)
    generate_validation_artifacts(y_test, y_pred, le, artifacts_dir)

    # --- Save Model and Preprocessors ---
    logging.info("Saving supervised model and preprocessors...")
    Path(artifacts_dir).mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, Path(artifacts_dir) / "supervised_model.pkl")
    joblib.dump(scaler, Path(artifacts_dir) / "supervised_scaler.pkl")
    joblib.dump(le, Path(artifacts_dir) / "label_encoder.pkl")
    logging.info("Supervised artifacts saved successfully. ✅")
    
    logging.info("--- Supervised Validation Pipeline Finished ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate RFM features using a supervised classifier.")
    parser.add_argument(
        "--input",
        type=str,
        default="clustered_customer.csv", # CORRECTED: Pointing to the correct file by default
        help="Path to the input CSV with RFM features and a 'segments' column."
    )
    parser.add_argument(
        "--artifacts",
        type=str,
        default="artifacts",
        help="Directory to save validation artifacts."
    )
    args = parser.parse_args()

    validation_pipeline(
        input_path=args.input,
        artifacts_dir=args.artifacts,
        label_col="segments"
    )
