# 🏠 Real Estate Investment Advisor

**Predicting Property Profitability & Future Value**

---

## 📌 Project Overview

This project is a Machine Learning-based web application that helps real estate investors make informed decisions. It predicts:

* 📈 **Future Property Price (after 5 years)** *(Regression)*
* ✅ **Whether a property is a Good Investment or not** *(Classification)*

---

## 🚀 Live Demo

👉 **Try the app here:**
🔗 https://jyothi1235-real-estate-investment-advisor-app-zp7c2t.streamlit.app/

---

## 🎯 Problem Statement

Develop an intelligent system that:

* Classifies properties as **Good Investment** or **Not**
* Predicts **future property value after 5 years**
* Provides insights through a **Streamlit interactive application**
* Tracks experiments using MLflow

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
* Streamlit
* MLflow
* Matplotlib, Seaborn

---

## 📊 Dataset

**File:** `india_housing_prices.csv`

### Key Features:

* State, City
* BHK, Size, Property Type
* Price, Price per SqFt
* Nearby Schools, Hospitals
* Amenities, Security

---

## ⚙️ Approach

### 🔹 Data Preprocessing

* Removed duplicates
* Handled missing values
* Encoded categorical features
* Applied feature scaling

### 🔹 Feature Engineering

* Price per SqFt
* Age of Property
* Amenities Count
* School Score

### 🔹 Target Variables

* **Regression:** Future Price using growth formula
* **Classification:** Good Investment based on multi-factor logic

---

## 📈 Exploratory Data Analysis (EDA)

* Price distribution
* Size vs Price relationship
* Correlation heatmap
* Location-based trends

---

## 🤖 Models Used

* Random Forest Regressor
* Decision Tree Classifier

---

## 📊 Model Evaluation

* Regression: RMSE
* Classification: Accuracy, F1-score

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

### Install dependencies

```
pip install -r requirements.txt
```

### Run app

```
streamlit run app.py
```

---

## 📌 Results

* Built regression & classification models
* Achieved good prediction performance
* Developed an interactive dashboard

---

## 📚 Key Learnings

* Data preprocessing
* Feature engineering
* Model building & evaluation
* Streamlit deployment

---

## 🔮 Future Improvements

* Location-based growth prediction
* Real-time data integration
* Advanced ML models

---

## 👩‍💻 Author

**Jyothi Reddy M**

---

## ⭐ Conclusion

This project shows how machine learning can help make better real estate investment decisions using data-driven insights.

---
