import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load artifacts
kmeans = joblib.load("artifacts/kmeans_model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")
clf = joblib.load("artifacts/supervised_model.pkl")
sup_scaler = joblib.load("artifacts/supervised_scaler.pkl")
label_encoder = joblib.load("artifacts/label_encoder.pkl")


st.set_page_config(page_title="Customer Segmentation App", layout="wide")

st.title("🛍 Customer Segmentation Dashboard")
st.write("Upload customer data or enter RFM values to predict their segment.")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file with Recency, Frequency, Monetary columns", type="csv")

def predict_segments(df):
    # Unsupervised clustering
    X_scaled = scaler.transform(df[["Recency", "Frequency", "Monetary"]])
    clusters = kmeans.predict(X_scaled)
    df["Cluster"] = clusters

    # Supervised segment classification
    X_scaled_sup = sup_scaler.transform(df[["Recency", "Frequency", "Monetary"]])
    seg_pred = clf.predict(X_scaled_sup)
    df["PredictedSegment"] = label_encoder.inverse_transform(seg_pred)

    return df

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.dataframe(data.head())

    if all(col in data.columns for col in ["Recency", "Frequency", "Monetary"]):
        results = predict_segments(data)
        st.subheader("Predicted Results")
        st.dataframe(results.head())

        # Visualization
        st.subheader("Cluster Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x="PredictedSegment", data=results, ax=ax, palette="Set2")
        st.pyplot(fig)
    else:
        st.error("Uploaded CSV must contain Recency, Frequency, Monetary columns.")

# Manual input
st.sidebar.subheader("Manual Prediction")
r = st.sidebar.number_input("Recency (days since last purchase)", min_value=0, max_value=400, value=50)
f = st.sidebar.number_input("Frequency (number of orders)", min_value=1, max_value=500, value=5)
m = st.sidebar.number_input("Monetary (total spend)", min_value=1.0, max_value=50000.0, value=1000.0)

if st.sidebar.button("Predict Segment"):
    df_input = pd.DataFrame([[r, f, m]], columns=["Recency", "Frequency", "Monetary"])
    result = predict_segments(df_input)
    st.sidebar.success(f"Predicted Segment: {result['PredictedSegment'][0]}")
    st.sidebar.info(f"Cluster ID: {result['Cluster'][0]}") 
