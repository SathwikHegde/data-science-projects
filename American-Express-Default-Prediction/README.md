# American Express Customer Default Prediction

## Overview

This project focuses on predicting the probability that a customer will **default** on their credit card balance in the future. We use the [American Express Default Prediction dataset from Kaggle](https://www.kaggle.com/competitions/amex-default-prediction/data), which includes anonymized and aggregated customer profile data. Each record represents a snapshot of a customer’s financial behavior over time.

---

## Objective

Predict whether a customer will **default** (`target=1`) or **not default** (`target=0`) based on features derived from their historical monthly profiles, including:

- `D_*`: Delinquency variables  
- `S_*`: Spend variables  
- `P_*`: Payment variables  
- `B_*`: Balance variables  
- `R_*`: Risk variables

---

## Dataset Description

| File | Description |
|------|-------------|
| `train_data.csv` | Contains 200,000 rows of training customer data |
| `train_labels.csv` | Labels corresponding to the training data |
| `test_data.csv` | Contains 200,000 rows for evaluation |

---

## Data Preprocessing

We applied extensive preprocessing steps:
- **Redundant Column Removal**: Dropped transaction timestamps
- **Null Value Handling**: Explored different imputation strategies using Mean, Median, and Mode
- **Feature Transformation**: Skew correction and scaling
- **Dimensionality Reduction**: Performed **Principal Component Analysis (PCA)** for feature decorrelation

---

## Exploratory Data Analysis

- Visualized distribution of spend, balance, delinquency, and risk features
- Observed that many spend variables were **skewed**
- Identified weak correlations among most spend features
- Examined time-series patterns in customer behavior

---

## Modeling & Evaluation

We tested multiple machine learning models, both with and without hyperparameter tuning:

### Models Used
1. **Logistic Regression**
2. **XGBoost**
3. **Random Forest Classifier**
4. **Support Vector Machine**

### Hyperparameter Tuning Methods
- **GridSearchCV**
- **RandomizedSearchCV**
- **BayesSearchCV**

### Model Evaluation Metrics
- Accuracy
- Precision/Recall (optional for binary classification)
- Visualization of performance comparison

---

## Results

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 87.21% |
| XGBoost (Base) | 88.62% |
| XGBoost (RandomizedSearchCV) | 89.25% |
| XGBoost (BayesSearchCV) | 90.02% |
| Random Forest (Base) | **90.46%** |
| Random Forest (GridSearchCV) | 90.25% |
| Support Vector Machine | 86.44% |

**Best Performing Model:**  
`RandomForestClassifier` without hyperparameter tuning gave the highest accuracy of **90.46%**

---

## Conclusion

- Advanced ensemble methods like **Random Forest** and **XGBoost** outperformed linear models
- Hyperparameter tuning offered marginal gains, but sometimes reduced performance (as seen in RandomForestClassifier)
- This framework can be extended to real-time risk scoring pipelines for financial institutions

---

## Project Structure

```
American-Express-Default-Prediction/
│
├── American_Express_Default_Prediction.ipynb      # Main analysis notebook
├── American Express Default Prediction- Summary.pptx  # Presentation slides
├── train_data.csv                                  # Training dataset (external)
├── train_labels.csv                                # Training labels (external)
├── test_data.csv                                   # Testing dataset (external)
├── README.md                                       # Project overview
├── .gitignore                                      # Git ignored files
```

---

## Disclaimer

This project uses anonymized, public data from Kaggle for academic and educational purposes only. No proprietary or sensitive information is disclosed.

---

## Author

**Sathwik Hegde**