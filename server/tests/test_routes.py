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
        [[0.] * NUMBER_OF_FEATURES,
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
    assert response.json() == {"Labels": [0, 0]}
