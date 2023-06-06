import io
from typing import Union

import matplotlib.pyplot as plt
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from .utils import get_path

router = APIRouter()

_data: Union[pd.DataFrame, None] = None


@router.get("/plot/{index}")
async def get_ecg_plot(index: int):
    global _data

    if _data is None:
        _data = get_data()
    check_index_bounds(index)
    img = make_plot_image(_data, index)
    return StreamingResponse(img, media_type="image/jpeg")


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


def make_plot_image(_data, index):
    plt.plot(_data.iloc[index], color="blue")
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.clf()
    return buffer
