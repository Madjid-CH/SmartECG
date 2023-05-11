import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from usecases.plotting import router as plotting_router
from usecases.predection import router as prediction_router

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


def main():
    configure()
    uvicorn.run(app)


def configure():
    configure_routers()
    configure_middleware()


def configure_routers():
    app.include_router(plotting_router)
    app.include_router(prediction_router)


def configure_middleware():
    origins = [
        "http://localhost:3000"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__":
    main()
else:
    configure()
