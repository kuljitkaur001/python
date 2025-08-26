# 03_supervised_validation.py
# Supervised validation using Logistic Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from pathlib import Path

def load_data(path="clustered_customer.csv"):
    """Load the labeled customer dataset (with 'segments' column)."""
    return pd.read_csv(path)

def train_supervised(rfm: pd.DataFrame, label_col="segments"):
    # Features = RFM values
    X = rfm[["Recency", "Frequency", "Monetary"]]
    
    # Labels = provided segments
    y = rfm[label_col]

    # Encode string labels -> numbers
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train Logistic Regression
    clf = LogisticRegression(max_iter=500, random_state=42)
    clf.fit(X_train_scaled, y_train)

    # Evaluate
    y_pred = clf.predict(X_test_scaled)
    print("Classification Report:\n", classification_report(y_test, y_pred, target_names=le.classes_))

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=le.classes_, yticklabels=le.classes_)
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix")
    plt.show()

    # Save model + label encoder + scaler
    Path("artifacts").mkdir(exist_ok=True)
    joblib.dump(clf, "artifacts/supervised_model.pkl")
    joblib.dump(scaler, "artifacts/supervised_scaler.pkl")
    joblib.dump(le, "artifacts/label_encoder.pkl")
    print("Saved Logistic Regression model + preprocessing objects ✅")

if __name__ == "__main__":
    rfm = load_data()   # loads clustered_customer.csv
    train_supervised(rfm, label_col="segments")
