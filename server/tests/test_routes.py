import shutil

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


@pytest.fixture
def create_temp_csv(tmp_path):
    NUMBER_OF_FEATURES = 188
    data = pd.DataFrame(
        [[0] * NUMBER_OF_FEATURES,
         [0] * NUMBER_OF_FEATURES]
    )
    path = tmp_path / "test.csv"
    data.to_csv(path, index=False)
    yield path
    shutil.rmtree(tmp_path)


def test_predict_csv(create_temp_csv):
    with open(create_temp_csv, "rb") as f:
        response = client.post("/predict", files={"file": f})

    assert response.status_code == 200
    assert response.json() == {"Labels": [0, 0]}
