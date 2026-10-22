 [README.md](https://github.com/user-attachments/files/33801185/README.md)

# 🌾 Tamil Nadu Crop Production & Rainfall Analysis (2024-25)

An end-to-end data analytics project that explores **district-wise crop production, rainfall and crop yield in Tamil Nadu** using **Power BI** for interactive dashboards and **Python (Random Forest)** for yield prediction.

---

## 📌 Project Overview

Tamil Nadu's agriculture depends heavily on monsoon rainfall and irrigation. This project:

- Analyses **38 districts** for foodgrains, sugarcane and groundnut production
- Compares **actual vs normal rainfall** across districts
- Studies the relationship between **irrigation and rice yield**
- Builds a **machine learning model** to predict crop yield and honestly evaluates how well it performs

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| Visualization | Power BI Desktop |
| Programming | Python |
| Libraries | Pandas, NumPy, Scikit-learn |
| ML Model | Random Forest Regressor |
| Validation | Leave-One-Out Cross-Validation |

---

## 📊 Dashboard Preview

### Page 1 – Overview Dashboard
![Overview Dashboard](screenshots/page1_overview.png)

**Highlights**
- KPI cards: Total Foodgrains (**11.0 M t**), Total Sugarcane (**13.3 M t**), Avg Annual Rainfall (**1.3K mm**), Avg Paddy Irrigation (**94 %**)
- Map of foodgrains production by district
- Top districts by rice production (Tiruvannamalai, Thanjavur, Tiruvarur…)
- Annual rainfall: actual vs normal
- Yield by crop and Rice Yield vs Paddy Irrigation scatter plot

### Page 2 – ML Insights Dashboard
![ML Insights Dashboard](screenshots/page2_ml_insights.png)

**Highlights**
- Model R², Error Reduction %, number of districts modelled
- Crop slicer (Groundnut / Maize / Rice)
- Actual vs Predicted yield by district
- Factor-group importance (Rainfall, Irrigation, Crop area)
- Model RMSE vs baseline RMSE gauge
- District-level error table

---

## 🗂️ Data Model

Tables loaded into Power BI:

| Table | Description |
|---|---|
| `master` | District-level production, area, yield, rainfall and irrigation data (38 rows) |
| `yield_long` | Crop yield in long format (District, Crop, Yield) |
| `ml_pred` | Actual vs predicted yield and error per district |
| `ml_imp` | Importance of each factor group per crop |
| `ml_sum` | Model metrics per crop (RMSE, MAE, R², baseline RMSE, verdict) |

Tables are connected through **Crop** and **District** keys (see model view).

---

## 🤖 Machine Learning Approach

- **Target:** Crop yield (t/ha) for Rice, Groundnut and Maize
- **Features:** Rainfall (SW monsoon, NE monsoon, winter, hot weather), irrigation %, crop area
- **Model:** Random Forest Regressor (300 trees, `min_samples_leaf=3`)
- **Validation:** Leave-One-Out Cross-Validation (suitable for the small number of districts)
- **Baseline:** Predicting the mean yield of the other districts
- **Feature importance:** Permutation importance, grouped into Rainfall / Irrigation / Crop area

### 📈 Results

| Crop | Districts | RMSE | Baseline RMSE | R² | Error Reduction | Verdict |
|---|---|---|---|---|---|---|
| Rice | 36 | 0.430 | 0.519 | 0.273 | 17 % | Weak model |
| Groundnut | 35 | 0.653 | 0.762 | 0.221 | 14 % | Weak model |
| Maize | 27 | 1.611 | 1.504 | -0.238 | -7 % | No useful model |

### 🔍 Key Insights

- The model beats the simple baseline for **Rice** and **Groundnut**, but only modestly.
- For **Maize**, the model performs worse than the baseline, so it is not reliable.
- **Rice yield** is driven mostly by crop area (39 %) and irrigation (35 %); **Groundnut** and **Maize** yield depend mostly on rainfall (88 % and 74 %).
- Limitations: only one year of data (2024-25) and ~27–36 districts, so predictions are limited. More years of data and soil/temperature features would improve accuracy.

---

## 📁 Project Structure

```
├── data/
│   ├── tn_2024_25_master_dataset.csv
│   ├── yield_long.csv
│   ├── ml_pred.csv
│   ├── ml_imp.csv
│   └── ml_sum.csv
├── dashboard/
│   └── my_project.pbix
├── scripts/
│   └── tn-crop-yield-powerbi-ml.py
├── screenshots/
│   ├── page1_overview.png
│   └── page2_ml_insights.png
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/Abinaya8125/tn-crop-yield-powerbi-ml.git
   cd tn-crop-yield-powerbi-ml
   ```
2. Install the required libraries
   ```bash
   pip install pandas numpy scikit-learn
   ```
3. Run the ML script (input dataset, output folder)
   ```bash
   python scripts/tn-crop-yield-powerbi-ml.py data/tn_2024_25_master_dataset.csv data
   ```
   This regenerates `ml_pred.csv`, `ml_imp.csv` and `ml_sum.csv`.
4. Open `dashboard/my_project.pbix` in **Power BI Desktop** and click **Refresh** (update the CSV file paths if needed).

---

## 🚀 Future Improvements

- Add multi-year data (2020–2025) for stronger models
- Include soil type, temperature and fertilizer usage
- Try Gradient Boosting / XGBoost and compare with Random Forest
- Publish the dashboard to Power BI Service

---

## 👩‍💻 Author

**Abinaya M**
B.Tech – Artificial Intelligence & Data Science
Arasu Engineering College, Kumbakonam

📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/abinaya-m-494a90332)
