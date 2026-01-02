import uvicorn
from fastapi import FastAPI

from .config.database import Base, engine
from .api.v1 import routers

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Invoice Backend",
    description="Invoice backend",
    version="0.1.0",
)

app.include_router(routers.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app)
