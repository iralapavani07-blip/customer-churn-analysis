import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Info:")
print(df.info())

# ----------------------------
# Churn Distribution
# ----------------------------
print("\nChurn Distribution:")
print(df["Churn"].value_counts())

plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.savefig("outputs/churn_distribution.png")
plt.show()

# ----------------------------
# Contract vs Churn
# ----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Churn by Contract Type")
plt.savefig("outputs/contract_churn.png")
plt.show()

# ----------------------------
# Monthly Charges vs Churn
# ----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Monthly Charges vs Churn")
plt.savefig("outputs/monthly_charges_churn.png")
plt.show()

# ----------------------------
# Encode categorical variables
# ----------------------------
df_encoded = df.copy()

for column in df_encoded.columns:
    if df_encoded[column].dtype == "object":
        df_encoded[column] = df_encoded[column].astype("category").cat.codes

print("\nEncoded Dataset Preview:")
print(df_encoded.head())

# ----------------------------
# Separate features and target
# ----------------------------
X = df_encoded.drop("Churn", axis=1)
y = df_encoded["Churn"]

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)

# ----------------------------
# Train-Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# ----------------------------
# Train Model
# ----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ----------------------------
# Predictions
# ----------------------------
y_pred = model.predict(X_test)

# ----------------------------
# Model Evaluation
# ----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ----------------------------
# Feature Importance
# ----------------------------
importance = pd.Series(model.coef_[0], index=X.columns)
importance = importance.sort_values(ascending=False)

plt.figure(figsize=(10,6))
importance.plot(kind="bar")
plt.title("Feature Importance for Churn Prediction")
plt.savefig("outputs/feature_importance.png")
plt.show()