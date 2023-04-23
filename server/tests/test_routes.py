import shutil

import pytest
from fastapi.testclient import TestClient
import pandas as pd
from server.main import app
from server.usecases.predection import Features

client = TestClient(app)


@pytest.fixture
def dummy_features():
    features = Features(
        duration=0,
        protocol_type="tcp",
        service="http",
        flag="SF",
        src_bytes=0,
        dst_bytes=0,
        land=0,
        wrong_fragment=0,
        urgent=0,
        hot=0,
        num_failed_logins=0,
        logged_in=0,
        num_compromised=0,
        root_shell=0,
        su_attempted=0,
        num_root=0,
        num_file_creations=0,
        num_shells=0,
        num_access_files=0,
        num_outbound_cmds=0,
        is_host_login=0,
        is_guest_login=0,
        count=0,
        srv_count=0,
        serror_rate=0,
        srv_serror_rate=0,
        rerror_rate=0,
        srv_rerror_rate=0,
        same_srv_rate=0,
        diff_srv_rate=0,
        srv_diff_host_rate=0,
        dst_host_count=0,
        dst_host_srv_count=0,
        dst_host_same_srv_rate=0,
        dst_host_diff_srv_rate=0,
        dst_host_same_src_port_rate=0,
        dst_host_srv_diff_host_rate=0,
        dst_host_serror_rate=0,
        dst_host_srv_serror_rate=0,
        dst_host_rerror_rate=0,
        dst_host_srv_rerror_rate=0,
    )
    return features.dict()


def test_predict_one(dummy_features):
    response = client.post("/predict/individual", json=dummy_features)
    assert response.status_code == 200
    assert response.json() == {"Labels": [0]}


@pytest.fixture
def create_temp_csv(tmp_path):
    data = pd.DataFrame(
        {
            "duration": [0, 0],
            "protocol_type": ["tcp", "tcp"],
            "service": ["http", "http"],
            "flag": ["SF", "SF"],
            "src_bytes": [0, 0],
            "dst_bytes": [0, 0],
            "land": [0, 0],
            "wrong_fragment": [0, 0],
            "urgent": [0, 0],
            "hot": [0, 0],
            "num_failed_logins": [0, 0],
            "logged_in": [0, 0],
            "num_compromised": [0, 0],
            "root_shell": [0, 0],
            "su_attempted": [0, 0],
            "num_root": [0, 0],
            "num_file_creations": [0, 0],
            "num_shells": [0, 0],
            "num_access_files": [0, 0],
            "num_outbound_cmds": [0, 0],
            "is_host_login": [0, 0],
            "is_guest_login": [0, 0],
            "count": [0, 0],
            "srv_count": [0, 0],
            "serror_rate": [0, 0],
            "srv_serror_rate": [0, 0],
            "rerror_rate": [0, 0],
            "srv_rerror_rate": [0, 0],
            "same_srv_rate": [0, 0],
            "diff_srv_rate": [0, 0],
            "srv_diff_host_rate": [0, 0],
            "dst_host_count": [0, 0],
            "dst_host_srv_count": [0, 0],
            "dst_host_same_srv_rate": [0, 0],
            "dst_host_diff_srv_rate": [0, 0],
            "dst_host_same_src_port_rate": [0, 0],
            "dst_host_srv_diff_host_rate": [0, 0],
            "dst_host_serror_rate": [0, 0],
            "dst_host_srv_serror_rate": [0, 0],
            "dst_host_rerror_rate": [0, 0],
            "dst_host_srv_rerror_rate:": [0, 0],
        }
    )
    path = tmp_path / "test.csv"
    data.to_csv(path, index=False)
    yield path
    shutil.rmtree(tmp_path)


def test_predict_csv(create_temp_csv):
    with open(create_temp_csv, "rb") as f:
        response = client.post("/predict/batch", files={"file": f})

    assert response.status_code == 200
    assert response.json() == {"Labels": [0, 0]}
