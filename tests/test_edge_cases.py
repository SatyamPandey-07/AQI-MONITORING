import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pytest

def test_empty_dataframe():
    df = pd.DataFrame()
    assert df.empty

def test_all_missing_values():
    df = pd.DataFrame({'A': [np.nan, np.nan], 'B': [np.nan, np.nan]})
    assert df.isnull().all().all()

def test_single_class():
    X = np.random.rand(10, 3)
    y = np.zeros(10)
    model = RandomForestClassifier()
    with pytest.raises(ValueError):
        model.fit(X, y)

def test_scaler_on_constant_column():
    X = np.ones((10, 3))
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    assert np.allclose(X_scaled, 0)

def test_label_encoder_unseen():
    le = LabelEncoder()
    y_train = ['A', 'B']
    le.fit(y_train)
    with pytest.raises(ValueError):
        le.transform(['C'])
