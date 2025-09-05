# ⏳ Survival Modeling and Risk Stratification of Cardiovascular Patients

This project applies **survival analysis techniques** to study how long patients with cardiovascular conditions survive under different risk factors. Instead of simple classification, the focus is on **time-to-event modeling** (days until death or survival) using statistical and machine learning methods.  

The project also includes an **interactive Streamlit dashboard** where users can upload datasets and perform their own exploratory and survival analyses.

---

## 🎯 Objectives
- Perform **exploratory data analysis (EDA)** on patient data  
- Estimate survival probabilities with **Kaplan–Meier curves**  
- Identify significant risk factors using **Cox Proportional Hazards regression**  
- Apply **Random Survival Forest (RSF)** for non-linear survival modeling  
- Provide an **interactive dashboard** for dataset exploration and modeling  

---

## 📊 Dataset
The default dataset used is the [UCI Heart Failure Clinical Records dataset](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records), containing **299 patients** with follow-up data.  

Key features include:
- `time` → follow-up period (days)  
- `DEATH_EVENT` → event indicator (1 = died, 0 = survived)  
- Clinical attributes: `age`, `sex`, `anaemia`, `diabetes`, `ejection_fraction`, `serum_creatinine`, `serum_sodium`, `platelets`, etc.  

---

## 📈 Methods Applied
1. **EDA**  
   - Feature distributions  
   - Correlation heatmaps  
   - Survival distributions by subgroups  

2. **Survival Models**  
   - Kaplan–Meier survival curves  
   - Cox Proportional Hazards regression (hazard ratios)  
   - Random Survival Forest (RSF) survival function estimation  

3. **Comparison with Standard Classification Models**  
   - Logistic Regression  
   - Random Forest  
   - XGBoost  

---

## 🖥️ Interactive Dashboard (Streamlit)
The Streamlit dashboard allows users to:  
- 📂 Upload their own dataset (must include `time` and `DEATH_EVENT` columns)  
- 🔎 Explore data distributions & correlations  
- 📉 Generate Kaplan–Meier survival curves  
- ⚖️ Fit Cox models with user-selected features  
- 🌲 Train Random Survival Forest and visualize survival predictions  

### Run the Dashboard:
```bash
streamlit run app_survival.py
🚀 Installation
Clone the repository and install dependencies:

bash
git clone https://github.com/your-username/cardiovascular-survival-analysis.git
cd cardiovascular-survival-analysis

pip install -r requirements.txt

▶️ Usage
Place your dataset (or use the default heart failure dataset) in the data/ folder

Run the analysis script or Jupyter notebook:

bash
python survival_analysis.py
Or launch the Streamlit dashboard:

bash
streamlit run app_survival.py

🔬 Results
Kaplan–Meier analysis showed clear survival differences across subgroups

Cox regression identified low ejection fraction and high serum creatinine as major risk drivers

RSF achieved a C-index ~0.79, capturing non-linear survival patterns