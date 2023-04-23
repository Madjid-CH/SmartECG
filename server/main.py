import uvicorn
from fastapi import FastAPI

from usecases.predection import router

app = FastAPI()


def main():
    configure()
    uvicorn.run(app)


def configure():
    configure_routers()


def configure_routers():
    app.include_router(router)


if __name__ == "__main__":
    main()
else:
    configure()
