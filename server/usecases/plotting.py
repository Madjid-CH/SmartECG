import matplotlib.pyplot as plt
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from typing import Union
from .utils import get_path

router = APIRouter()

_data: Union[pd.DataFrame, None] = None


@router.get("/plot/{index}")
async def get_ecg_plot(index: int):
    global _data

    if _data is None:
        _data = get_data()
    check_index_bounds(index)
    path = make_plot_path(_data, index)
    return FileResponse(path)


def get_data():
    global _data
    try:
        path = get_path("\\data\\data.csv")
        return pd.read_csv(path, header=None)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail="No data to plot.")


def check_index_bounds(index):
    global _data
    if not 0 <= index < len(_data):
        raise HTTPException(status_code=400, detail="Index out of bounds")


def make_plot_path(_data, index):
    plt.plot(_data.iloc[index], color="blue")
    path = get_path(f"\\plots\\{index}.jpg")
    plt.savefig(path)
    plt.clf()
    return path