import os
import shutil

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


@pytest.fixture
def dummy_dataframe():
    NUMBER_OF_FEATURES = 187
    return pd.DataFrame(
        [[1.] * NUMBER_OF_FEATURES,
         [0.] * NUMBER_OF_FEATURES]
    )


@pytest.fixture
def create_temp_csv(dummy_dataframe, tmp_path):
    path = tmp_path / "test.csv"
    dummy_dataframe.to_csv(path, index=False, header=False)
    yield path
    shutil.rmtree(tmp_path)


def test_predict_csv(create_temp_csv):
    with open(create_temp_csv, "rb") as f:
        response = client.post("/predict", files={"file": f})

    assert response.status_code == 200
    assert response.json() == {'Labels': ['Normal', 'Normal']}


def test_get_ecg_plot_success():
    response = client.get("/plot/0")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"


def test_get_ecg_plot_index_out_of_bounds():
    response = client.get("/plot/999999")
    assert response.status_code == 400
    assert response.json() == {"detail": "Index out of bounds"}