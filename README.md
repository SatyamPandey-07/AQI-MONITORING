<div align="center">
  <img src="https://img.icons8.com/fluency/96/air-quality.png" width="80"/>
  <h1>AQI Monitoring Web App</h1>
  <p><b>Interactive Air Quality Analysis, Visualization, and Machine Learning Prediction</b></p>
  <p>
    <img src="https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=flat&logo=streamlit&logoColor=white"/>
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python"/>
    <img src="https://img.shields.io/badge/License-MIT-green"/>
    <img src="https://img.shields.io/badge/Tests-Pytest-blueviolet"/>
  </p>
</div>

> **A beautiful, modern web app for exploring, modeling, and predicting Air Quality Index (AQI) using machine learning.**

---

## 🚀 Features

- 📊 **Data Exploration**: Visualize AQI data, distributions, and correlations
- 🧹 **Preprocessing**: Handle missing values, remove outliers, and select features
- 🤖 **Modeling**: Train Random Forest, Logistic Regression, or XGBoost models
- 🏆 **Evaluation**: View classification reports, confusion matrices, and feature importances
- 🔮 **Prediction**: Instantly predict AQI category for new data
- 💾 **Model Saving/Loading**: Save and reload trained models
- 🧪 **Testing**: Automated tests for data and edge cases
- 🎨 **Modern UI**: Clean, responsive, and user-friendly interface

---

## 🌈 App Preview

<p align="center">
  <img src="screenshots/app_main_ui.png" width="600"/>
  <br>
  <img src="screenshots/model_results.png" width="600"/>
  <br>
  <img src="screenshots/outlier_visualization.png" width="600"/>
  <br>
  <i>Replace these with your actual screenshots for best effect!</i>
</p>

---

## 🛠️ Quick Start

```bash
# 1. Clone the repository
 git clone <your-repo-url>
 cd aqi-monitoring

# 2. Create and activate a virtual environment
 python -m venv .venv
 .venv\Scripts\activate  # On Windows
 # Or
 source .venv/bin/activate  # On Mac/Linux

# 3. Install dependencies
 pip install -r requirements.txt

# 4. Run the Streamlit app
 streamlit run app.py
```

---

## 📝 Usage

- Use the sidebar to upload data, select preprocessing, features, and model
- Train and evaluate with a click
- Predict AQI for new data instantly
- Visualize results and download models

---

## 📁 Project Structure

```
├── app.py                # Main Streamlit web app
├── config.py             # Configuration file
├── requirements.txt      # Python dependencies
├── data/                 # Raw and processed data files
├── models/               # Saved models and scalers
├── notebooks/            # Jupyter notebooks (EDA, preprocessing, training, evaluation)
├── tests/                # Unit and edge-case tests
└── screenshots/          # App screenshots (add your own!)
```

---

## ✅ Testing

Automated tests are provided in `tests/`.

```bash
pytest tests/
```

---

## 💡 Model Saving/Loading

The app saves and loads models automatically in the `models/` directory.

```python
import joblib
# Save model
joblib.dump(model, 'models/aqi_model.pkl')
# Load model
model = joblib.load('models/aqi_model.pkl')
```

---

## 🔍 Data Validation

- Built-in checks for missing values, class balance, and outliers
- Outlier visualization and feature importance explanations included

---

## 🙌 Credits

- Built with [Streamlit](https://streamlit.io/), [scikit-learn](https://scikit-learn.org/), [XGBoost](https://xgboost.ai/), and [pandas](https://pandas.pydata.org/)
- UI icons by [Icons8](https://icons8.com/icons/set/air-quality)

---

## 📄 License

MIT License
