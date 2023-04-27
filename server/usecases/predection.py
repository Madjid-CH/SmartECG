import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pydantic import BaseModel


class Features(BaseModel):
    """Features for ECG Heartbeat Categorization Dataset"""


class Model:
    def __init__(self):
        self.model = None

    def predict(self, data):
        # TODO: Implement model prediction
        return [0] * len(data)


model = Model()
router = APIRouter()


@router.post("/predict")
async def predict_batch(file: UploadFile = File(...)):
    if file.filename.endswith(".csv"):
        data = pd.read_csv(file.file)
        return {
            "Labels": model.predict(data)
        }
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid file format. Only CSV Files accepted.")


