# 🏠 House Price Prediction

A machine learning project that predicts California house prices using a Random Forest Regressor with hyperparameter tuning, deployed as an interactive Streamlit web app.

##  Project Structure

```
House-Price-Prediction/
├── data/
│   └── housing.csv          # California housing dataset
├── model/
│   └── full_model.pkl       # Trained model (generated after running notebook)
├── main.ipynb               # Training & inference notebook
├── app.py                   # Streamlit web app
├── requirements.txt         # Python dependencies
└── README.md
```

##  Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/whosharvari/House-Price-Prediction.git
cd House-Price-Prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model
Open and run `main.ipynb` in Jupyter. On the first run (when no model exists), it will:
- Load and split the dataset using stratified sampling
- Engineer features (`rooms_per_household`, `bedrooms_per_room`, `population_per_household`)
- Run GridSearchCV to find the best hyperparameters
- Save the trained model to `model/full_model.pkl`
- Print cross-validation RMSE

On subsequent runs (model already exists), it runs inference on the held-out test set and saves predictions to `data/output.csv`.

### 4. Run the web app
```bash
streamlit run app.py
```

##  Model Details

| Component | Detail |
|---|---|
| Algorithm | Random Forest Regressor |
| Tuning | GridSearchCV (3-fold CV) |
| Features | 12 (original + engineered) |
| Preprocessing | Median imputation, StandardScaler, OneHotEncoding |
| Dataset | California Housing (~20,000 records) |

**Hyperparameter grid searched:**
- `n_estimators`: 100, 200
- `max_depth`: 10, 20, None
- `min_samples_split`: 2, 5

##  Web App

The Streamlit app accepts user inputs for all housing features and returns a predicted median house value in USD.

**Inputs:** Longitude, Latitude, Housing Median Age, Total Rooms, Total Bedrooms, Population, Households, Median Income, Ocean Proximity

##  Dependencies

```
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
streamlit
```

##  👤 Author
Sharvari Mude
