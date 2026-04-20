# 🏠 Real Estate Investment Advisor

**Predicting Property Profitability & Future Value**

---

## 📌 Project Overview

This project is a Machine Learning-based web application that helps real estate investors make informed decisions. It predicts:

* 📈 **Future Property Price (after 5 years)** *(Regression)*
* ✅ **Whether a property is a Good Investment or not** *(Classification)*

The system uses data-driven insights and domain-based feature engineering to provide accurate recommendations.

---

## 🎯 Problem Statement

Develop an intelligent system that:

* Classifies properties as **Good Investment** or **Not**
* Predicts **future property value after 5 years**
* Provides insights through a **Streamlit interactive application**
* Tracks experiments using **MLflow**

---

## 💼 Business Use Cases

* Assist investors in identifying high-return properties
* Help buyers choose properties in growing locations
* Enable real estate companies to automate investment analysis
* Increase trust using data-backed predictions

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Machine Learning (Regression & Classification)
* Streamlit (UI Deployment)
* MLflow (Experiment Tracking)
* Matplotlib, Seaborn (EDA Visualization)

---

## 📊 Dataset

**File:** `india_housing_prices.csv`

### Key Features:

* Location: State, City
* Property Info: BHK, Size, Type
* Price Details: Price, Price per SqFt
* Infrastructure: Schools, Hospitals, Transport
* Amenities & Facilities

---

## ⚙️ Approach

### 🔹 Data Preprocessing

* Removed duplicates
* Handled missing values
* Encoded categorical features
* Feature scaling applied

### 🔹 Feature Engineering

* Price per SqFt
* Age of Property
* Amenities Count
* School Score

### 🔹 Target Variables

* **Regression:** Future Price using growth formula
* **Classification:** Good Investment based on multi-factor rules

---

## 📈 Exploratory Data Analysis (EDA)

* Price distribution analysis
* Size vs Price relationship
* Correlation heatmap
* Location-based trends

---

## 🤖 Models Used

* **Regression:** Random Forest Regressor
* **Classification:** Decision Tree Classifier

---

## 📊 Model Evaluation

* **Regression:** RMSE, MAE
* **Classification:** Accuracy, F1-score, Confusion Matrix

---

## 🚀 Streamlit Application

Features:

* User input form
* Predicts:

  * Future price
  * Investment recommendation
* Interactive UI

---

## 📁 Project Structure

```
├── app.py
├── project.ipynb
├── india_housing_prices.csv
├── reg_model.pkl
├── clf_model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run Streamlit app

```
streamlit run app.py
```

---

## 📌 Results

* Successfully built regression & classification models
* Achieved low RMSE for price prediction
* Developed an interactive Streamlit dashboard
* Implemented feature-based investment logic

---

## 📚 Key Learnings

* Data preprocessing & feature engineering
* Model building & evaluation
* Real-world problem solving
* Streamlit deployment
* MLflow experiment tracking

---

## 🔮 Future Improvements

* Add location-based growth rates
* Integrate real-time data
* Improve model accuracy with advanced algorithms
* Deploy on cloud (Streamlit Cloud / AWS)

---

## 👩‍💻 Author

**Jyothi Reddy M**

---

## ⭐ Conclusion

This project demonstrates how machine learning can assist in making smart real estate investment decisions using data-driven insights.

---
