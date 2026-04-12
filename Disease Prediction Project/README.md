# 🧠 Disease Prediction Using Machine Learning

A complete end-to-end **Machine Learning pipeline** that predicts diseases based on patient symptoms using multiple classification models.

---

## 🚀 Project Overview

This project builds an intelligent system that takes **patient symptoms as input** and predicts the most probable disease.

* ✅ Handles **132 symptoms** as input features
* ✅ Predicts among **41 diseases**
* ✅ Trains and compares **5 ML models**
* ✅ Outputs **top 3 probable diseases with confidence**

---

## 📊 Dataset Information

| Attribute        | Details                 |
| ---------------- | ----------------------- |
| Training Samples | 4920                    |
| Testing Samples  | 42                      |
| Features         | 132 (Binary Symptoms)   |
| Target Classes   | 41 Diseases             |
| Data Type        | 0 (Absent), 1 (Present) |

---

## ⚙️ Machine Learning Models Used

* 🌳 Decision Tree
* 🌲 Random Forest
* 📊 Naive Bayes
* 🔵 Support Vector Machine (SVM)
* 🚀 Gradient Boosting

---

## 📈 Workflow Pipeline

```
Data Collection → Data Cleaning → EDA → Preprocessing → Model Training → Evaluation → Prediction → Deployment Ready
```

---

## 🔍 Exploratory Data Analysis (EDA)

* ✔ Balanced dataset (equal samples per disease)
* ✔ Top frequent symptoms identified
* ✔ Correlation heatmap of symptoms
* ✔ Visualization of disease distribution

---

## 🧪 Model Training & Evaluation

* Models trained on full dataset
* Accuracy compared on test dataset
* Best model selected automatically

📊 Evaluation Metrics:

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## 🏆 Best Model

The model with the highest test accuracy is automatically selected:

```
Best Model: <Auto-detected during execution>
```

---

## 💾 Model Saving

The trained model is saved as:

```
disease_model.pkl
```

Includes:

* Trained model
* Label encoder
* Feature list

---

## 🔮 Prediction System

### Function:

```python
predict_disease(symptoms_list)
```

### Example:

```python
patient_symptoms = [
    'itching',
    'skin_rash',
    'nodal_skin_eruptions'
]

result = predict_disease(patient_symptoms)
print(result)
```

### Output:

```
Top 3 Predictions:
Allergy                                  92.3%
Fungal infection                         5.1%
Drug Reaction                            2.6%

>>> Predicted Disease: Allergy
```

---

## 📁 Project Structure

```
├── Training.csv
├── Testing.csv
├── disease_model.pkl
├── notebook.ipynb
└── README.md
```

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Pickle

---

## 📌 Key Features

✔ Multi-model comparison
✔ Automatic best model selection
✔ Real-time disease prediction
✔ Top-3 probability output
✔ Feature importance visualization

---

## ⚠️ Disclaimer

> This project is for **educational purposes only** and should NOT be used as a substitute for professional medical advice.

---

## 🤝 Contribution

Feel free to fork this repo, improve models, or integrate it into a web/app system.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
