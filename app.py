"""
AQI Monitoring Web App
---------------------
A Streamlit application for air quality analysis, visualization, and AQI prediction using machine learning.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
import config

try:
	from xgboost import XGBClassifier
	xgb_available = True
except ImportError:
	xgb_available = False


st.set_page_config(page_title="Air Quality AQI Classifier", layout="wide")

# Sidebar logo/title and instructions
st.sidebar.markdown("""
<div style='text-align: center;'>
	<img src='https://img.icons8.com/fluency/96/air-quality.png' width='60'>
	<h2 style='margin-bottom:0;'>AQI Monitor</h2>
</div>
""", unsafe_allow_html=True)
st.sidebar.info("""
**Instructions:**
- Upload your data or use the default
- Choose preprocessing and features
- Select a model and train
- Predict AQI for new data
""")

st.markdown("""
<h1 style='color:#2E8B57;'>🌍 Air Quality Analysis & AQI Prediction</h1>
<hr style='border:1px solid #2E8B57;'>
""", unsafe_allow_html=True)

# --- Data Upload ---
st.sidebar.header("1. Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"], help="Upload your air quality data in CSV format.")
if uploaded_file:
	df = pd.read_csv(uploaded_file)
else:
	df = pd.read_csv("data/processed_aqi.csv")
	st.sidebar.info("Using default processed_aqi.csv")

# --- Data Preprocessing ---
st.sidebar.header("2. Preprocessing Options")
missing_strategy = st.sidebar.selectbox(
	"Handle missing values:", ["Fill with mean", "Fill with median", "Drop rows"], index=0,
	help="Choose how to handle missing values in your data.")

# Optionally remove outliers using Z-score
remove_outliers = st.sidebar.checkbox("Remove outliers (Z-score > 3)")

# Drop rows with missing AQI_Bucket (target)
df = df.dropna(subset=["AQI_Bucket"])

# Fill/drop missing values for numeric columns
df_numeric = df.select_dtypes(include=[np.number]).columns.tolist()
if missing_strategy == "Fill with mean":
	# Fill missing values with mean
	df[df_numeric] = df[df_numeric].fillna(df[df_numeric].mean())
elif missing_strategy == "Fill with median":
	# Fill missing values with median
	df[df_numeric] = df[df_numeric].fillna(df[df_numeric].median())
else:
	# Drop rows with any missing values
	df = df.dropna()

# Remove outliers if selected
if remove_outliers:
	# Z-score outlier detection
	z_scores = np.abs((df[df_numeric] - df[df_numeric].mean()) / df[df_numeric].std(ddof=0))
	outlier_mask = (z_scores > 3).any(axis=1)
	n_outliers = outlier_mask.sum()
	df = df[~outlier_mask]
	st.sidebar.info(f"Removed {n_outliers} outlier rows.")

# Convert Date column
if "Date" in df.columns:
	df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
	df["Year"] = df["Date"].dt.year
	df["Month"] = df["Date"].dt.month
	df["Day"] = df["Date"].dt.day
	df["Season"] = df["Date"].dt.month % 12 // 3 + 1

# Encode categorical features
for col in ["City", "Station"]:
	if col in df.columns:
		df[col] = LabelEncoder().fit_transform(df[col].astype(str))

# Encode target
label_enc = LabelEncoder()
df["AQI_Bucket"] = label_enc.fit_transform(df["AQI_Bucket"].astype(str))

# Drop irrelevant columns
if "Station" in df.columns and df["Station"].nunique() > 0.5 * len(df):
	df = df.drop(columns=["Station"])

# --- Feature Selection ---
all_features = [c for c in df.columns if c not in ["AQI_Bucket", "Date"]]
selected_features = st.sidebar.multiselect(
	"Select features for modeling:", all_features, default=all_features,
	help="Choose which features to use for model training.")


X = df[selected_features]
y = df["AQI_Bucket"]


# --- Remove classes with <2 samples ---
class_counts = y.value_counts()
valid_classes = class_counts[class_counts >= 2].index
mask = y.isin(valid_classes)
X = X[mask]
y = y[mask]

# --- Re-encode target after filtering to ensure consecutive classes ---
label_enc_filtered = LabelEncoder()
y = label_enc_filtered.fit_transform(y)
class_names_filtered = label_enc_filtered.classes_

# --- Check for empty data after filtering ---
if X.shape[0] == 0 or y.shape[0] == 0:
	st.error("No data available for training after filtering classes with less than 2 samples. Please check your data or preprocessing options.")
	st.stop()

# --- Feature Scaling ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- Train-Test Split ---
st.sidebar.header("3. Train-Test Split")
test_size = st.sidebar.slider("Test size (%)", 10, 50, 20)
X_train, X_test, y_train, y_test = train_test_split(
	X_scaled, y, test_size=test_size/100, stratify=y, random_state=42)

# --- Model Selection ---
st.sidebar.header("4. Model Selection")
model_name = st.sidebar.selectbox(
	"Choose model:", ["Random Forest", "Logistic Regression"] + (["XGBoost"] if xgb_available else []),
	help="Select a machine learning model for AQI prediction.")

if model_name == "Random Forest":
	model = RandomForestClassifier(n_estimators=200, random_state=42)
elif model_name == "Logistic Regression":
	model = LogisticRegression(max_iter=1000, random_state=42)
else:
	# XGBoost for multiclass classification
	num_classes = len(np.unique(y))
	model = XGBClassifier(
		use_label_encoder=False,
		eval_metric='mlogloss',
		objective='multi:softprob',
		num_class=num_classes,
		random_state=42
	)

# --- Model Training ---
if st.sidebar.button("Train Model"):
	# Train the selected model
	model.fit(X_train, y_train)
	y_pred = model.predict(X_test)
	unique_labels = np.unique(np.concatenate([y_test, y_pred]))
	class_names = label_enc.inverse_transform(unique_labels)

	# Show classification report
	st.subheader("Classification Report")
	st.text(classification_report(y_test, y_pred, labels=unique_labels, target_names=class_names))

	# Show confusion matrix
	st.subheader("Confusion Matrix")
	fig, ax = plt.subplots(figsize=(8,6))
	sns.heatmap(confusion_matrix(y_test, y_pred, labels=unique_labels), annot=True, fmt="d", cmap="Blues",
				xticklabels=class_names, yticklabels=class_names, ax=ax)
	plt.xlabel("Predicted")
	plt.ylabel("Actual")
	st.pyplot(fig)

	# Show feature importances if available
	st.subheader("Feature Importances")
	if hasattr(model, "feature_importances_"):
		importances = model.feature_importances_
		if len(importances) == len(selected_features):
			feat_imp = pd.Series(importances, index=selected_features).sort_values(ascending=False)
			st.bar_chart(feat_imp)
			st.markdown("**Explanation:** Higher values indicate features that contribute more to the model's predictions.")
		else:
			st.warning(f"Cannot display feature importances: model returned {len(importances)} importances, but {len(selected_features)} features are selected. This may happen if the model uses internal feature expansion or encoding.")
	elif hasattr(model, "coef_"):
		importances = np.abs(model.coef_).flatten()
		if len(importances) == len(selected_features):
			feat_imp = pd.Series(importances, index=selected_features).sort_values(ascending=False)
			st.bar_chart(feat_imp)
			st.markdown("**Explanation:** Higher absolute coefficient values indicate more important features for the model.")
		else:
			st.warning(f"Cannot display feature importances: model returned {len(importances)} importances, but {len(selected_features)} features are selected. This may happen if the model uses internal feature expansion or encoding.")


	# Always save model and scaler after training using config paths
	model_path = os.path.abspath(config.MODEL_PATH)
	scaler_path = os.path.abspath(config.SCALER_PATH)
	try:
		joblib.dump(model, model_path)
		st.sidebar.success(f"Model saved as {model_path}")
		joblib.dump(scaler, scaler_path)
		st.sidebar.success(f"Scaler saved as {scaler_path}")
	except Exception as e:
		st.sidebar.error(f"Error saving model or scaler: {e}")

	st.success("Model trained and evaluated!")
	st.balloons()


	st.session_state['model'] = model
	st.session_state['scaler'] = scaler
	st.session_state['class_names_filtered'] = class_names_filtered
	st.session_state['selected_features'] = selected_features
	st.session_state['X'] = X

# Model loading
elif st.sidebar.button("Load Model"):
	model_path = os.path.abspath(config.MODEL_PATH)
	scaler_path = os.path.abspath(config.SCALER_PATH)
	try:
		model = joblib.load(model_path)
		scaler = joblib.load(scaler_path)
		st.sidebar.success(f"Model and scaler loaded from {model_path} and {scaler_path}.")
		st.session_state['model'] = model
		st.session_state['scaler'] = scaler
		st.session_state['class_names_filtered'] = class_names_filtered
		st.session_state['selected_features'] = selected_features
		st.session_state['X'] = X
	except Exception as e:
		st.sidebar.error(f"Error loading model or scaler: {e}")
else:
	st.info("Click 'Train Model' in the sidebar to start training.")

# --- Predict on new data (always available if model is loaded or trained) ---
if 'model' in st.session_state and 'scaler' in st.session_state:
	st.markdown("""
	<h3 style='color:#4682B4;'>Predict AQI Category for New Data</h3>
	""", unsafe_allow_html=True)
	input_data = {}
	X_ref = st.session_state['X'] if 'X' in st.session_state else X
	cols = st.columns(len(st.session_state['selected_features']))
	for i, feat in enumerate(st.session_state['selected_features']):
		val = cols[i].number_input(f"{feat}", value=float(X_ref[feat].mean()))
		input_data[feat] = val
	if st.button("Predict AQI Category"):
		input_df = pd.DataFrame([input_data])
		input_scaled = st.session_state['scaler'].transform(input_df)
		pred = st.session_state['model'].predict(input_scaled)
		st.success(f"**Predicted AQI Category:** {st.session_state['class_names_filtered'][pred[0]]}")

# --- Data Preview ---
with st.expander("Show Raw Data"):
	st.dataframe(df.head(100))

# --- Data Visualization ---
with st.expander("Show Data Visualizations"):
	st.markdown("<h4 style='color:#8B0000;'>AQI Bucket Distribution</h4>", unsafe_allow_html=True)
	fig, ax = plt.subplots()
	sns.countplot(x=label_enc.inverse_transform(df["AQI_Bucket"]), ax=ax)
	plt.xticks(rotation=45)
	st.pyplot(fig)

	st.markdown("<h4 style='color:#8B0000;'>Correlation Heatmap</h4>", unsafe_allow_html=True)
	fig2, ax2 = plt.subplots(figsize=(10,8))
	sns.heatmap(df[selected_features + ["AQI_Bucket"]].corr(), annot=True, cmap="coolwarm", ax=ax2)
	st.pyplot(fig2)

# --- Footer ---
st.markdown("""
<hr>
<div style='text-align:center; color:gray;'>
	AQI Monitoring App &copy; 2025 | Built with Streamlit
</div>
""", unsafe_allow_html=True)
