# 🩺 Breast Cancer Prediction System

An end-to-end **Machine Learning** project for predicting whether a breast tumor is **Benign** or **Malignant** using the **Breast Cancer Wisconsin Dataset**. Multiple classification algorithms were evaluated, and **Random Forest** was selected as the best model for deployment.

## 📌 Project Overview

The project analyzes breast cancer diagnostic data, preprocesses the dataset, selects relevant features, trains and evaluates multiple classification models, and deploys the selected model using **Streamlit**.

The original dataset contains **569 rows and 33 columns**.

## 🎯 Objective

To build a machine learning classification system that uses tumor measurements to predict the breast cancer diagnosis as:

- 🟢 **Benign**
- 🔴 **Malignant**

> This project is for educational and machine-learning demonstration purposes and is not a substitute for professional medical diagnosis.

## 📊 Dataset

**Dataset:** Breast Cancer Wisconsin Dataset

Initial dataset shape:

```text
569 rows × 33 columns
```

The project performs data cleaning by removing unnecessary columns such as:

- `id`
- `Unnamed: 32`

The target variable is:

```text
diagnosis
```

The diagnosis is label encoded into numerical classes for machine learning.

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Outlier Treatment
   ↓
Target Label Encoding
   ↓
Correlation Analysis & Feature Selection
   ↓
StandardScaler
   ↓
70/30 Train-Test Split
   ↓
Train Multiple Classification Models
   ↓
Model Evaluation & Comparison
   ↓
Select Best Model — Random Forest
   ↓
Save Model, Scaler & Feature Names
   ↓
Streamlit Deployment
   ↓
Benign / Malignant Prediction
```

## 🤖 Models Evaluated

The notebook explores and evaluates multiple classification algorithms, including:

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- Bagging
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost
- LightGBM
- Artificial Neural Network (ANN)

Models are compared using training/testing performance and classification metrics. Based on the final model comparison in the notebook, **Random Forest** is selected as the best model and saved for deployment.

## ⚙️ Data Preprocessing

The project includes:

- Removal of unnecessary columns
- Outlier treatment
- Label encoding of the target
- Correlation analysis
- Feature selection
- Standardization using `StandardScaler`
- Train-test splitting

The dataset is partitioned using:

```python
train_test_split(X, y, test_size=0.3, random_state=42)
```

This gives approximately:

- **70% Training Data**
- **30% Testing Data**

## 📈 Model Evaluation

The notebook uses multiple evaluation techniques, including:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report
- ROC Curve / ROC-AUC
- Cross-validation
- GridSearchCV for model tuning

## 🌲 Final Model

**Random Forest Classifier**

The final Random Forest model is serialized using Python's `pickle` module along with the preprocessing scaler and selected feature names.

```text
model.pkl
scaler.pkl
features.pkl
```

Saving these objects ensures that the Streamlit application uses the same trained model, preprocessing transformation, and feature structure used during model development.

## 💻 Streamlit Web Application

The project includes a simple Streamlit interface where users can enter tumor feature measurements.

The application:

1. Loads `model.pkl`.
2. Loads `scaler.pkl`.
3. Loads `features.pkl`.
4. Generates an input field for every required feature.
5. Converts the entered values into a Pandas DataFrame.
6. Applies the saved scaler.
7. Sends the transformed values to the trained model.
8. Displays the prediction.

### Prediction Results

```text
🔴 Malignant Tumor
```

or

```text
🟢 Benign Tumor
```

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- TensorFlow / Keras
- Matplotlib
- Seaborn
- Streamlit
- Pickle
- Jupyter Notebook

## 📁 Project Structure

```text
Breast-Cancer-Prediction/
│
├── app.py
├── cancer_prediction_code.ipynb
├── data.csv
├── model.pkl
├── scaler.pkl
├── features.pkl
└── README.md
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Breast-Cancer-Prediction
```

### 2. Install dependencies

```bash
pip install pandas numpy scikit-learn xgboost lightgbm tensorflow streamlit matplotlib seaborn
```

### 3. Make sure the deployment files are present

```text
app.py
model.pkl
scaler.pkl
features.pkl
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application should then open in your web browser.

## 🔍 Deployment Pipeline

```text
User Input
    ↓
Pandas DataFrame
    ↓
Saved StandardScaler
    ↓
Random Forest Model
    ↓
Prediction
    ↓
Benign / Malignant
```

## ✨ Key Features

- Complete machine learning classification workflow
- Exploratory analysis and preprocessing
- Multiple ML model comparison
- Hyperparameter tuning
- Cross-validation
- Random Forest final model
- Saved preprocessing pipeline components
- Interactive Streamlit deployment
- Real-time Benign/Malignant prediction

## ⚠️ Disclaimer

This application is developed for **educational and research demonstration purposes only**. Its output must not be interpreted as medical advice, a confirmed diagnosis, or a recommendation for treatment. Consult a qualified healthcare professional for medical evaluation and decisions.

## 👩‍💻 Author

**Lekha Sree Annam**

B.Tech — Computer Science and Engineering  
Artificial Intelligence & Machine Learning

**Skills:** Python | Machine Learning | Data Science | Pandas | Scikit-learn | Random Forest | Streamlit

---

⭐ If you find this project useful, consider giving the repository a star.
