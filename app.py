import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter, CoxPHFitter

st.set_page_config(page_title="Survival Analysis Dashboard", layout="wide")
st.title("🫀 General Survival Analysis Dashboard")

uploaded = st.file_uploader("Upload dataset (CSV)", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    df.columns = df.columns.str.lower()
else:
    st.info("No file uploaded. Using default Heart Failure dataset.")
    df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
    df.columns = df.columns.str.lower()

rename_map = {}
if "event" not in df.columns and "death_event" in df.columns:
    rename_map["death_event"] = "event"
df = df.rename(columns=rename_map)

if not {"time", "event"}.issubset(df.columns):
    st.error("Dataset must contain 'time' and 'event' columns (event=0/1).")
    st.stop()

st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

st.subheader("🔎 Data Exploration")
col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df["event"].value_counts())
with col2:
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=False, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

st.subheader("📉 Kaplan–Meier Survival Analysis")
kmf = KaplanMeierFitter()
kmf.fit(durations=df["time"], event_observed=df["event"], label="All Patients")
fig, ax = plt.subplots()
kmf.plot_survival_function(ax=ax)
ax.set_title("Overall Survival Curve")
st.pyplot(fig)
st.markdown(f"**Median Survival Time**: {kmf.median_survival_time_:.1f} days")

categorical_cols = df.select_dtypes(include=["int","object","category","bool"]).columns.tolist()
categorical_cols = [c for c in categorical_cols if c not in ["time","event"]]

if categorical_cols:
    strat_col = st.selectbox("Stratify by:", categorical_cols)
    fig, ax = plt.subplots()
    for val, subset in df.groupby(strat_col):
        km = KaplanMeierFitter()
        km.fit(subset["time"], subset["event"], label=f"{strat_col}={val}")
        km.plot_survival_function(ax=ax)
    ax.set_title(f"KM Curve by {strat_col}")
    st.pyplot(fig)

st.subheader("⚖️ Cox Proportional Hazards Model")
covariates = st.multiselect("Select covariates", [c for c in df.columns if c not in ["time","event"]])
if covariates:
    cph = CoxPHFitter()
    cph.fit(df[["time","event"]+covariates], duration_col="time", event_col="event")
    st.write(cph.summary)
    cph.plot()
    st.pyplot(plt.gcf())
