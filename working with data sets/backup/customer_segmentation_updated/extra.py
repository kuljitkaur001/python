# src/app.py
# Advanced, multi-page Streamlit dashboard for Customer Segmentation

import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Professional Styling ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# This is a more robust way to apply styles
st.markdown("""
<style>
    /* Main app background */
    .main {
        background-color: #F54927;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        color: white;
    }
    /* Title styling */
    h1, h2, h3 {
        color: #1e3a8a; /* A deep blue for titles */
    }
    /* Custom button styling */
    .stButton>button {
        color: white;
        background-color: #1e3a8a;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #2563eb; /* A lighter blue on hover */
    }
    /* Styling for expanders */
    .stExpander {
        border: 1px solid #d1d5db;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


# --- Caching Functions for Performance ---
@st.cache_resource
def load_artifacts():
    """
    Loads all the pre-trained models and preprocessors.
    Using st.cache_resource ensures these are loaded only once.
    """
    artifacts = {}
    artifact_dir = Path("artifacts")
    try:
        artifacts["kmeans_model"] = joblib.load(artifact_dir / "kmeans_model.pkl")
        artifacts["scaler"] = joblib.load(artifact_dir / "scaler.pkl")
        artifacts["supervised_model"] = joblib.load(artifact_dir / "supervised_model.pkl")
        artifacts["supervised_scaler"] = joblib.load(artifact_dir / "supervised_scaler.pkl")
        artifacts["label_encoder"] = joblib.load(artifact_dir / "label_encoder.pkl")
        return artifacts
    except FileNotFoundError:
        st.error("Could not find model artifacts. Please run the training scripts first.")
        return None

@st.cache_data
def predict_segments(_artifacts, df):
    """
    Performs both unsupervised and supervised prediction on the input data.
    Using st.cache_data to avoid re-running predictions on the same data.
    """
    # Unsupervised clustering
    X_scaled = _artifacts["scaler"].transform(df[["Recency", "Frequency", "Monetary"]])
    df["Cluster"] = _artifacts["kmeans_model"].predict(X_scaled)

    # Supervised segment classification
    X_scaled_sup = _artifacts["supervised_scaler"].transform(df[["Recency", "Frequency", "Monetary"]])
    seg_pred = _artifacts["supervised_model"].predict(X_scaled_sup)
    df["Segment"] = _artifacts["label_encoder"].inverse_transform(seg_pred)
    
    return df

# --- Helper Functions ---
def df_to_csv(df):
    """Converts a DataFrame to a CSV string for downloading."""
    return df.to_csv(index=False).encode('utf-8')

# --- Main Application ---
artifacts = load_artifacts()

if artifacts:
    st.sidebar.title("Dashboard Navigation")
    page = st.sidebar.radio(
        "Go to",
        ("Project Overview", "Explore Segments", "Single Prediction", "Model Performance")
    )

    # --- Page 1: Project Overview ---
    if page == "Project Overview":
        st.title("🛍️ Customer Segmentation Project")
        st.markdown("""
        This interactive dashboard is the final product of a comprehensive data science pipeline for customer segmentation. 
        The goal is to group customers based on their purchasing behavior using the **RFM (Recency, Frequency, Monetary)** framework.
        """)
        
        st.subheader("Methodology")
        st.markdown("""
        1.  **Feature Engineering:** Customer transaction data is processed to calculate RFM values for each customer.
        2.  **Unsupervised Learning:** A **K-Means clustering** algorithm is trained on the scaled RFM data to discover natural groupings or 'clusters' of customers.
        3.  **Supervised Validation:** A **Logistic Regression** model is trained to validate how well RFM features can predict predefined customer segments, confirming the business value of these metrics.
        4.  **Interactive Dashboard:** This Streamlit application serves as the user interface to interact with the trained models, explore data, and gain insights.
        """)
        
        st.subheader("Actionable Insights")
        st.markdown("Translating data segments into business strategy:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("VIP / High Value")
            st.write("These are your most loyal and valuable customers. Focus on retention and loyalty programs.")
        with col2:
            st.warning("Potential Loyalists / At Risk")
            st.write("These customers are active but could churn. Engage them with personalized offers.")
        with col3:
            st.error("Churned / Low Value")
            st.write("These customers are inactive. Target them with win-back campaigns or reduce marketing spend.")


        with st.expander("What is RFM Analysis?"):
            st.markdown("""
            - **Recency:** How recently a customer has made a purchase.
            - **Frequency:** How often a customer makes a purchase.
            - **Monetary:** How much money a customer spends.
            
            These three metrics are powerful indicators of a customer's value and engagement.
            """)

    # --- Page 2: Explore Segments ---
    elif page == "Explore Segments":
        st.title("🔎 Explore Customer Segments")
        st.write("Upload a CSV file with customer RFM data to see their predicted segments and explore the results.")

        uploaded_file = st.file_uploader(
            "Upload your input CSV file", type=["csv"],
            help="The CSV should contain 'Recency', 'Frequency', and 'Monetary' columns."
        )

        if uploaded_file:
            data = pd.read_csv(uploaded_file)
            st.info(f"File '{uploaded_file.name}' uploaded successfully with {data.shape[0]} rows.")

            if all(col in data.columns for col in ["Recency", "Frequency", "Monetary"]):
                results = predict_segments(artifacts, data)
                
                st.subheader("Segmentation Results")
                st.dataframe(results.head())
                
                st.download_button(
                    label="📥 Download Full Results as CSV",
                    data=df_to_csv(results),
                    file_name="segmented_customers.csv",
                    mime="text/csv",
                )
                
                st.header("📊 Dashboard")
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Segment Distribution")
                    segment_counts = results["Segment"].value_counts()
                    fig = px.pie(values=segment_counts.values, names=segment_counts.index, title="Customer Segments",
                                 color_discrete_sequence=px.colors.qualitative.Bold)
                    st.plotly_chart(fig, use_container_width=True)

                with col2:
                    st.subheader("RFM Segment Averages")
                    segment_means = results.groupby("Segment")[["Recency", "Frequency", "Monetary"]].mean().reset_index()
                    fig = px.bar(segment_means, x="Segment", y=["Recency", "Frequency", "Monetary"], barmode='group', 
                                 title="Average RFM per Segment", color_discrete_sequence=px.colors.qualitative.Bold)
                    st.plotly_chart(fig, use_container_width=True)

                st.subheader("Interactive 3D Scatter Plot")
                fig3d = px.scatter_3d(results, x='Recency', y='Frequency', z='Monetary', color='Segment',
                                      title="3D View of Customer Segments",
                                      labels={'Recency': 'Recency (Days)', 'Frequency': 'Frequency (Orders)', 'Monetary': 'Monetary (Value)'},
                                      color_discrete_sequence=px.colors.qualitative.Bold)
                st.plotly_chart(fig3d, use_container_width=True)

            else:
                st.error("Error: The uploaded CSV must contain 'Recency', 'Frequency', and 'Monetary' columns.")

    # --- Page 3: Single Prediction ---
    elif page == "Single Prediction":
        st.title("🔮 Predict a Single Customer's Segment")
        st.write("Enter the RFM values for a single customer to get an instant segment prediction.")

        with st.form("prediction_form"):
            st.subheader("Enter Customer RFM Values")
            recency = st.number_input("Recency (days since last purchase)", min_value=0, value=50, step=1)
            frequency = st.number_input("Frequency (total number of orders)", min_value=1, value=5, step=1)
            monetary = st.number_input("Monetary (total spend)", min_value=0.0, value=1000.0, step=50.0)
            
            submitted = st.form_submit_button("Predict Segment")

        if submitted:
            input_df = pd.DataFrame([[recency, frequency, monetary]], columns=["Recency", "Frequency", "Monetary"])
            result = predict_segments(artifacts, input_df)
            predicted_segment = result['Segment'][0]
            
            st.success(f"## Predicted Segment: **{predicted_segment}**")
            
            st.write("This prediction indicates the customer's likely behavior based on the model trained on historical data.")


    # --- Page 4: Model Performance ---
    elif page == "Model Performance":
        st.title("📈 Model Performance Evaluation")
        st.write("Here you can review the performance artifacts generated during the model training and validation phases.")

        tab1, tab2 = st.tabs(["Unsupervised Model (K-Means)", "Supervised Validation (Logistic Regression)"])

        with tab1:
            st.header("K-Means Clustering Evaluation")
            st.write("The 'Elbow Method' is used to find a good value for 'k' (the number of clusters). We look for an 'elbow' in the plot where the rate of decrease in error sharply changes.")
            
            elbow_plot_path = Path("artifacts/elbow_plot.png")
            if elbow_plot_path.exists():
                st.image(str(elbow_plot_path), caption="Elbow Method Plot for K-Means")
            else:
                st.warning("Elbow plot not found. Please run the model training script.")

        with tab2:
            st.header("Supervised Model Validation")
            st.write("A Logistic Regression model was trained to see if RFM values can effectively predict known customer segments. High performance here indicates that RFM is a strong framework for this dataset.")
            
            cm_plot_path = Path("artifacts/confusion_matrix.png")
            report_path = Path("artifacts/classification_report.txt")

            if cm_plot_path.exists():
                st.image(str(cm_plot_path), caption="Confusion Matrix")
            else:
                st.warning("Confusion matrix plot not found. Please run the validation script.")

            if report_path.exists():
                st.subheader("Classification Report")
                report_text = report_path.read_text()
                st.code(report_text, language="text")
            else:
                st.warning("Classification report not found. Please run the validation script.")
