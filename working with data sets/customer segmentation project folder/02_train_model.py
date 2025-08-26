# src/02_train_model.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib
from pathlib import Path
import matplotlib.pyplot as plt

def load_rfm(path="artifacts/rfm.csv"):
    return pd.read_csv(path)

def scale_features(rfm: pd.DataFrame):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])
    return X_scaled, scaler

def find_optimal_k(X_scaled, max_k=10):
    sse = []
    silhouette_scores = {}
    K = range(2, max_k+1)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        sse.append(kmeans.inertia_)
        silhouette_scores[k] = silhouette_score(X_scaled, kmeans.labels_)
    
    # plot elbow
    plt.figure(figsize=(8,5))
    plt.plot(K, sse, "o-")
    plt.xlabel("k")
    plt.ylabel("SSE")
    plt.title("Elbow Method")
    plt.show()

    print("Silhouette scores by k:")
    for k,v in silhouette_scores.items():
        print(f"k={k}: {v:.3f}")

def train_kmeans(X_scaled, k=4):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X_scaled)
    return model

def save_artifacts(model, scaler, out_dir="artifacts"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    joblib.dump(model, f"{out_dir}/kmeans_model.pkl")
    joblib.dump(scaler, f"{out_dir}/scaler.pkl")
    print(f"Saved model and scaler to {out_dir}/")

if __name__ == "__main__":
    rfm = load_rfm()
    X_scaled, scaler = scale_features(rfm)

    # Step 1: elbow + silhouette (visually decide k)
    find_optimal_k(X_scaled, max_k=10)

    # Step 2: choose best k (e.g., 4)
    model = train_kmeans(X_scaled, k=4)

    # Step 3: attach cluster labels to RFM
    rfm["Cluster"] = model.predict(X_scaled)
    print(rfm.head())

    # Step 4: save artifacts
    save_artifacts(model, scaler)
    rfm.to_csv("artifacts/rfm_with_clusters.csv", index=False)
