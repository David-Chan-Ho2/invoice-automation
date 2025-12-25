import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Backend",
    description="FastAPI backend",
    version="0.1.0",
)

if __name__ == "__main__":
    uvicorn.run(app)
