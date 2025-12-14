# src/02_train_model.py
# Automated, configurable model training pipeline

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib
from pathlib import Path
import matplotlib.pyplot as plt
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

def load_rfm_features(path: str) -> pd.DataFrame:
    """
    Loads the RFM features from a specified CSV file.

    Args:
        path (str): The path to the rfm.csv file.

    Returns:
        pd.DataFrame: DataFrame with RFM features.
    """
    logging.info(f"Loading RFM features from {path}...")
    try:
        rfm = pd.read_csv(path)
        logging.info("RFM features loaded successfully.")
        return rfm
    except FileNotFoundError:
        logging.error(f"Error: RFM file not found at {path}. Please run the feature building script first.")
        raise

def scale_features(rfm: pd.DataFrame) -> (pd.DataFrame, StandardScaler):
    """
    Scales the Recency, Frequency, and Monetary columns using StandardScaler.

    Args:
        rfm (pd.DataFrame): The RFM DataFrame.

    Returns:
        tuple: A tuple containing the scaled data (numpy array) and the fitted scaler object.
    """
    logging.info("Scaling RFM features...")
    scaler = StandardScaler()
    # Ensure we only scale the numeric RFM columns
    rfm_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])
    logging.info("Features scaled successfully.")
    return rfm_scaled, scaler

def find_and_visualize_optimal_k(X_scaled: pd.DataFrame, max_k: int, out_dir: str):
    """
    Calculates SSE and Silhouette scores to find the optimal number of clusters (k)
    and saves the elbow plot visualization.

    Args:
        X_scaled (pd.DataFrame): The scaled feature data.
        max_k (int): The maximum number of clusters to test.
        out_dir (str): The directory to save the elbow plot image.
    """
    logging.info(f"Searching for optimal k up to {max_k} clusters...")
    sse = []
    silhouette_scores = {}
    K = range(2, max_k + 1)

    for k in K:
        kmeans = KMeans(n_clusters=k, n_init=10, random_state=42) # Set n_init explicitly
        kmeans.fit(X_scaled)
        sse.append(kmeans.inertia_)
        score = silhouette_score(X_scaled, kmeans.labels_)
        silhouette_scores[k] = score
        logging.info(f"For k={k}, Silhouette Score is {score:.4f}")

    # --- Save Elbow Plot ---
    plt.figure(figsize=(10, 6))
    plt.plot(K, sse, "bo-")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Sum of Squared Errors (SSE)")
    plt.title("Elbow Method for Optimal k")
    plt.grid(True)
    
    plot_path = Path(out_dir) / "elbow_plot.png"
    plt.savefig(plot_path)
    logging.info(f"Elbow method plot saved to {plot_path}")
    plt.close() # Close the plot to prevent it from displaying in non-interactive environments

    # Log the best silhouette score
    best_k_silhouette = max(silhouette_scores, key=silhouette_scores.get)
    logging.info(f"Best k based on Silhouette Score: {best_k_silhouette} (Score: {silhouette_scores[best_k_silhouette]:.4f})")


def train_kmeans_model(X_scaled: pd.DataFrame, k: int) -> KMeans:
    """
    Trains the final KMeans model with the specified number of clusters.

    Args:
        X_scaled (pd.DataFrame): The scaled feature data.
        k (int): The chosen number of clusters.

    Returns:
        KMeans: The trained KMeans model object.
    """
    logging.info(f"Training final KMeans model with k={k}...")
    model = KMeans(n_clusters=k, n_init=10, random_state=42) # Set n_init explicitly
    model.fit(X_scaled)
    logging.info("KMeans model training complete.")
    return model

def save_artifacts(model: KMeans, scaler: StandardScaler, rfm_df: pd.DataFrame, out_dir: str):
    """
    Saves the trained model, scaler, and the final DataFrame with cluster labels.

    Args:
        model (KMeans): The trained KMeans model.
        scaler (StandardScaler): The fitted scaler.
        rfm_df (pd.DataFrame): The RFM data with the 'Cluster' column added.
        out_dir (str): The directory to save the artifacts.
    """
    logging.info(f"Saving artifacts to directory: {out_dir}")
    output_path = Path(out_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Save the model and scaler
    joblib.dump(model, output_path / "kmeans_model.pkl")
    joblib.dump(scaler, output_path / "scaler.pkl")

    # Save the clustered data
    rfm_df.to_csv(output_path / "rfm_with_clusters.csv", index=False)
    
    logging.info("Model, scaler, and clustered data saved successfully. ✅")

def training_pipeline(input_path: str, artifacts_dir: str, n_clusters: int, max_k_eval: int):
    """
    Orchestrates the full model training pipeline.

    Args:
        input_path (str): Path to the input rfm.csv file.
        artifacts_dir (str): Directory to save all output artifacts.
        n_clusters (int): The number of clusters (k) for the final model.
        max_k_eval (int): The max k to evaluate for the elbow plot.
    """
    logging.info("--- Starting Model Training Pipeline ---")
    
    rfm_features = load_rfm_features(input_path)
    X_scaled, scaler = scale_features(rfm_features)
    
    # Hyperparameter tuning step
    find_and_visualize_optimal_k(X_scaled, max_k=max_k_eval, out_dir=artifacts_dir)
    
    # Model training step
    final_model = train_kmeans_model(X_scaled, k=n_clusters)
    
    # Add cluster labels to the original RFM data
    rfm_features["Cluster"] = final_model.predict(X_scaled)
    
    # Save all results
    save_artifacts(final_model, scaler, rfm_features, out_dir=artifacts_dir)
    
    logging.info("--- Model Training Pipeline Finished ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a KMeans clustering model on RFM data.")
    parser.add_argument(
        "--input",
        type=str,
        default="artifacts/rfm.csv",
        help="Path to the input RFM CSV file."
    )
    parser.add_argument(
        "--artifacts",
        type=str,
        default="artifacts",
        help="Directory to save training artifacts (model, scaler, plots)."
    )
    parser.add_argument(
        "--k",
        type=int,
        default=4,
        help="The number of clusters (k) to use for the final model."
    )
    parser.add_argument(
        "--max_k",
        type=int,
        default=10,
        help="The maximum number of clusters to evaluate for the elbow plot."
    )
    args = parser.parse_args()

    training_pipeline(
        input_path=args.input,
        artifacts_dir=args.artifacts,
        n_clusters=args.k,
        max_k_eval=args.max_k
    )
