# Customer Churn Analysis & Prediction

## Dashboard Preview

![Customer Churn Dashboard](outputs/Dashboard_preview.jpeg)

## Project Overview

Customer churn is a major challenge for telecom companies.
This project analyzes customer churn using the **Telco Customer Churn dataset** and identifies the key factors influencing customer attrition.

The project combines **data analysis, machine learning, and interactive visualization** to generate actionable business insights.

---

## Dataset Information

Dataset: **Telco Customer Churn Dataset**

Total Customers: **7043**
Churned Customers: **1869**
Overall Churn Rate: **26.54%**

The dataset contains customer demographic information, account details, and service usage patterns.

---

## Project Architecture

```
Dataset
   ↓
Data Loading (Pandas)
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Encoding
   ↓
Train-Test Split
   ↓
Machine Learning Model (Logistic Regression)
   ↓
Model Evaluation
   ↓
Power BI Dashboard Visualization
```

---

## Technologies Used

Python
Pandas
NumPy
Matplotlib
Scikit-learn
Power BI

---

## Key Insights

• Customers with **month-to-month contracts churn the most**
• Customers using **electronic check payments show higher churn rates**
• **Higher monthly charges correlate with higher churn probability**
• Long-term contracts significantly **reduce churn risk**

---
## Model Performance

Model Used: Logistic Regression

Accuracy: ~80%  
Precision: ~74%  
Recall: ~65%  
F1 Score: ~69%

### Model Evaluation

![Model Results](outputs/model_results.png)

---

## Project Outputs

The project includes:

* Data analysis using Python
* Machine learning churn prediction model
* Visualizations for churn trends
* Interactive **Power BI dashboard**

---

## Dashboard Overview

The Power BI dashboard provides:

• Total customers
• Churned customers
• Churn rate KPI
• Internet service distribution
• Contract vs churn analysis
• Payment method insights
• Monthly charges vs churn analysis

---

## Business Value

The analysis helps telecom companies:

• Identify high-risk customers
• Improve customer retention strategies
• Optimize pricing and contract models
• Reduce churn and increase long-term revenue

---

## Future Improvements

• Deploy churn prediction model as an API
• Build real-time churn monitoring dashboard
• Apply advanced models such as Random Forest or XGBoost

