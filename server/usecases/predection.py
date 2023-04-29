import pandas as pd
import pandera as pa
from fastapi import APIRouter, UploadFile, File, HTTPException, status

columns_names = [f"x{i}" for i in range(188)]

schema = pa.DataFrameSchema({
    name: pa.Column(pa.Float, nullable=False)
    for name in columns_names
})


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
    check_is_csv_file(file)
    data = pd.read_csv(file.file, header=None, names=columns_names)
    validate_data(data)  # there is a huge performance penalty here
    return {
        "Labels": model.predict(data)
    }


def check_is_csv_file(file):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid file format. Only CSV Files accepted.")


def validate_data(data):
    try:
        schema.validate(data)

    except pa.errors.SchemaErrors:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid CSV file. Please check your file again.")
