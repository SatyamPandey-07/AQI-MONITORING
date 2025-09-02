import pandas as pd
import numpy as np
import pytest
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from app import df, all_features

def test_data_not_empty():
    assert not df.empty, "DataFrame should not be empty."

def test_no_missing_aqi_bucket():
    assert df['AQI_Bucket'].isnull().sum() == 0, "No missing AQI_Bucket values allowed."

def test_feature_scaling():
    scaler = StandardScaler()
    X = df[all_features]
    X_scaled = scaler.fit_transform(X)
    assert np.allclose(np.mean(X_scaled, axis=0), 0, atol=1e-1), "Features should be scaled to mean ~0."

def test_label_encoding():
    le = LabelEncoder()
    y = le.fit_transform(df['AQI_Bucket'].astype(str))
    assert set(y) == set(range(len(le.classes_))), "Labels should be consecutive integers."

def test_model_training():
    X = df[all_features]
    y = LabelEncoder().fit_transform(df['AQI_Bucket'].astype(str))
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    preds = model.predict(X)
    assert len(preds) == len(y), "Model should predict for all samples."
