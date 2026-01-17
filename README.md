
<div align="center">
  <img src="https://img.icons8.com/fluency/96/air-quality.png" width="90"/>
  <h1 style="font-size:2.5rem; margin-bottom:0;">AQI Monitoring Web App</h1>
  <p style="font-size:1.3rem; margin-top:0;">
    <b>🌫️ Interactive Air Quality Analysis, Visualization, and Machine Learning Prediction</b>
  </p>
  <p>
    <a href="https://streamlit.io/" target="_blank"><img src="https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=flat&logo=streamlit&logoColor=white"/></a>
    <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python"/></a>
    <img src="https://img.shields.io/badge/License-MIT-green"/>
    <img src="https://img.shields.io/badge/Tests-Pytest-blueviolet"/>
    <img src="https://img.shields.io/github/stars/SatyamPandey-07/AQI-MONITORING?style=social"/>
  </p>
</div>


<p align="center" style="font-size:1.1rem;">
  <b>✨ A beautiful, modern web app for exploring, modeling, and predicting Air Quality Index (AQI) using machine learning. ✨</b>
</p>

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

## 🎥 Live Demo

<div align="center">
  <b>🚀 See the AQI Monitoring App in action!</b><br><br>
  <a href="https://drive.google.com/file/d/1TcGlE-mTFIkVqMof7igcmiMlGWg0aZl0/view?usp=sharing" target="_blank">
    <img src="https://img.icons8.com/fluency/96/video-playlist.png" width="60"/>
    <br>
    <b>▶️ Watch Demo on Google Drive</b>
  </a>
  <br><br>
  <a href="live-video/Recording%202025-09-02%20162332%20(1).mp4" download>
    <img src="https://img.icons8.com/fluency/48/download--v1.png" width="32"/>
    <br>
    <b>⬇️ Download Demo Video (MP4, 80MB)</b>
  </a>
</div>

---

---

## 🌈 App Preview

<p align="center">
 <img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/5ecc7a76-abcf-45e7-9cb3-c8f5747f354a" />
  <br>
  <img width="1917" height="1076" alt="image" src="https://github.com/user-attachments/assets/6fb472b7-a683-4046-a2ad-f75e0293737c" />
  <br>
 <img width="1918" height="1048" alt="image" src="https://github.com/user-attachments/assets/60610d8e-a63c-44f8-a98c-a34bca46d3ec" />
  <br>
</p>

---


---

## ⚡ Quick Start

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


---

## 🧑‍� Usage

- Use the sidebar to upload data, select preprocessing, features, and model
- Train and evaluate with a click
- Predict AQI for new data instantly
- Visualize results and download models

---


---

## �️ Project Structure

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


---

## 🧪 Testing

Automated tests are provided in `tests/`.

```bash
pytest tests/
```

---


---

## � Model Saving/Loading

The app saves and loads models automatically in the `models/` directory.

```python
import joblib
# Save model
joblib.dump(model, 'models/aqi_model.pkl')
# Load model
model = joblib.load('models/aqi_model.pkl')
```

---


---

## 🧐 Data Validation

- Built-in checks for missing values, class balance, and outliers
- Outlier visualization and feature importance explanations included

---


---


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!<br>
Feel free to fork the repo, open an issue, or submit a pull request.

**How to contribute:**
- ⭐ Star this repo to show your support
- Fork the project
- Create your feature branch (`git checkout -b feature/AmazingFeature`)
- Commit your changes (`git commit -m 'Add some AmazingFeature'`)
- Push to the branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request

---

## 🙏 Credits

- Built with [Streamlit](https://streamlit.io/), [scikit-learn](https://scikit-learn.org/), [XGBoost](https://xgboost.ai/), [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/)
- UI icons by [Icons8](https://icons8.com/icons/set/air-quality)
- Project by [Satyam Pandey](https://github.com/SatyamPandey-07)

---

## 👤 Author

<b>Satyam Pandey</b>  
<a href="https://github.com/SatyamPandey-07" target="_blank">GitHub: @SatyamPandey-07</a>  
Email: satyampandey9820@gmail.com

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <img src="https://img.icons8.com/fluency/48/party-baloons.png" width="40"/>
  <h3>Made with ❤️ by Satyam Pandey</h3>
  <p>2025 &copy; All rights reserved.</p>
</div>

---


---

## 📄 License

MIT License
