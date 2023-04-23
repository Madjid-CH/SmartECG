import os

import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pydantic import BaseModel


class Features(BaseModel):
    """Features for KDD99 dataset"""
    duration: float
    protocol_type: str
    service: str
    flag: str
    src_bytes: float
    dst_bytes: float
    land: float
    wrong_fragment: float
    urgent: float
    hot: float
    num_failed_logins: float
    logged_in: float
    num_compromised: float
    root_shell: float
    su_attempted: float
    num_root: float
    num_file_creations: float
    num_shells: float
    num_access_files: float
    num_outbound_cmds: float
    is_host_login: float
    is_guest_login: float
    count: float
    srv_count: float
    serror_rate: float
    srv_serror_rate: float
    rerror_rate: float
    srv_rerror_rate: float
    same_srv_rate: float
    diff_srv_rate: float
    srv_diff_host_rate: float
    dst_host_count: float
    dst_host_srv_count: float
    dst_host_same_srv_rate: float
    dst_host_diff_srv_rate: float
    dst_host_same_src_port_rate: float
    dst_host_srv_diff_host_rate: float
    dst_host_serror_rate: float
    dst_host_srv_serror_rate: float
    dst_host_rerror_rate: float
    dst_host_srv_rerror_rate: float


class Model:
    def __init__(self):
        self.model = None

    def predict(self, data):
        # TODO: Implement model prediction
        return [0] * len(data)


model = Model()
router = APIRouter()


@router.post("/predict/individual")
async def predict(features: Features):
    data = pd.DataFrame([features.dict()])
    return {"Labels": model.predict(data)}


@router.post("/predict/batch")
async def predict_batch(file: UploadFile = File(...)):
    print(file.filename)

    if file.filename.endswith(".csv"):
        data = construct_dataframe_from(file)
        print(data.shape)
        os.remove(file.filename)
        return {
            "Labels": model.predict(data)
        }
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file format. Only CSV Files accepted.")


def construct_dataframe_from(file):
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    return pd.read_csv(file.filename)
