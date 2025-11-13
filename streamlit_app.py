
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="FuMind.ai Assignment", layout="wide")
st.title("Dashboard - ML Engineer Assignment")
st.markdown("This dashboard visualizes ERP + CMM data integration, schema matching, and quality analytics.")

# File uploader
prod_file = st.file_uploader("Upload Production Data (CSV)", type="csv", key="prod")
cmm_file = st.file_uploader("Upload CMM Data (CSV)", type="csv", key="cmm")

if prod_file and cmm_file:
    prod_df = pd.read_csv(prod_file)
    cmm_df = pd.read_csv(cmm_file)

    # Minimal schema mapping
    cmm_df = cmm_df.rename(columns={"component_id": "part_id"})
    prod_df.columns = [col.strip().lower().replace(" ", "_") for col in prod_df.columns]
    cmm_df.columns = [col.strip().lower().replace(" ", "_") for col in cmm_df.columns]

    # Parse timestamps
    prod_df["production_timestamp"] = pd.to_datetime(prod_df["production_timestamp"], errors="coerce")
    cmm_df["measurement_timestamp"] = pd.to_datetime(cmm_df["measurement_timestamp"], errors="coerce")

    # Join
    merged = pd.merge(cmm_df, prod_df, on=["part_id", "lot_id"], how="left")

    st.subheader("Unified Dataset")
    st.dataframe(merged.head(20))

    # Fail rates
    fail_by_feature = (
        merged[merged["result"] == "fail"]
        .groupby("feature_name")
        .size()
        .div(merged.groupby("feature_name").size())
        .fillna(0)
        .sort_values(ascending=False)
    )

    st.subheader("Fail Rate by Feature")
    fig, ax = plt.subplots()
    fail_by_feature.plot(kind="barh", ax=ax)
    st.pyplot(fig)

    # Pie chart
    st.subheader("Overall Pass/Fail Rate")
    result_counts = merged["result"].value_counts(normalize=True)
    fig2, ax2 = plt.subplots()
    result_counts.plot(kind="pie", autopct="%.1f%%", ax=ax2)
    ax2.set_ylabel("")
    st.pyplot(fig2)

else:
    st.info("Please upload both production and CMM CSV files to proceed.")