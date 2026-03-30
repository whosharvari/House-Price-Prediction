# 🏠 House Price Prediction

##  Overview

This project predicts house prices using machine learning by applying **data cleaning, exploratory data analysis (EDA), and feature engineering** to identify key price drivers.

---

##  Approach

* Cleaned data and handled missing values
* Performed EDA to understand feature relationships
* Engineered features to improve model performance
* Applied encoding and scaling using a pipeline
* Built and evaluated regression models using **scikit-learn**

---

##  Project Structure

```
house-price-prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── housing.csv
│
├── notebooks/
│   └── main.ipynb
│
└── model/
```

---

##  How to Run

1. Clone the repository

```
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Generate the model

* Open and run all cells in:

```
notebooks/main.ipynb
```

* This will create `full_model.pkl` locally

4. Run the Streamlit app

```
streamlit run app.py
```

---

## ⚠️ Note

The trained model file (`full_model.pkl`) is not included due to its large size.
Please run the notebook to generate it before using the app.

---

##  Tech Stack

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit

---

## Author
Sharvari Mude
