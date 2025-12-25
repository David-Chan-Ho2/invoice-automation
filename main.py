import uvicorn
from fastapi import FastAPI

from api import routers

app = FastAPI(
    title="FastAPI Backend",
    description="FastAPI backend",
    version="0.1.0",
)

app.include_router(routers.router)

if __name__ == "__main__":
    uvicorn.run(app)
