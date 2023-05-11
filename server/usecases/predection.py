import pandas as pd
import pandera as pa
from cachetools import cached
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from tensorflow import keras as tk

from .utils import get_path, hash_dataframe, get_a_cache

columns_names = [f"x{i}" for i in range(187)]

schema = pa.DataFrameSchema({
    name: pa.Column(pa.Float, nullable=False)
    for name in columns_names
})


class Model:
    def __init__(self):
        path = get_path("\\models\\model.h5", go_up_by=-2)
        self.model = tk.models.load_model(path)

    def predict(self, data):
        return self.model.predict(data)


model = Model()
router = APIRouter()


@router.post("/predict")
async def predict_batch(file: UploadFile = File(...)):
    check_is_csv_file(file)
    data = pd.read_csv(file.file, header=None, names=columns_names)
    validate_data(data)  # there is a huge performance penalty here
    save_data(data)
    return {
        "Labels": get_predictions(data)
    }


def check_is_csv_file(file):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid file format. Only CSV Files accepted.")


@cached(get_a_cache(), key=hash_dataframe)
def validate_data(data):
    try:
        schema.validate(data)
    except pa.errors.SchemaErrors:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid CSV file. Please check your file again.")


@cached(get_a_cache(), key=hash_dataframe)
def get_predictions(data):
    predictions = model.predict(data)
    predictions = predictions.argmax(axis=1).tolist()
    class_names = ["Normal",
                   "Artial Premature",
                   "Premature ventricular contraction",
                   "Fusion of ventricular and normal",
                   "Fusion of paced and normal"]
    predictions = [class_names[prediction] for prediction in predictions]
    return predictions


def save_data(data):
    path = get_path("\\data\\data.csv")
    data.to_csv(path, index=False, header=False)
