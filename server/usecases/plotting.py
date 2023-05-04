import matplotlib.pyplot as plt
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from .utils import get_path

router = APIRouter()

_data: pd.DataFrame | None = None


@router.get("/plot/{index}")
async def get_ecg_plot(index: int):
    global _data
    if _data is None:
        try:
            path = get_path("\\data\\data.csv")
            _data = pd.read_csv(path, header=None)
        except FileNotFoundError:
            return HTTPException(status_code=400, detail="No data to plot.")

    plt.plot(_data.iloc[index], color="blue")
    path = get_path(f"\\plots\\{index}.jpg")
    plt.savefig(path)
    return FileResponse(path)
