from fastapi import FastAPI
from minio_utils import get_minio_data
from superset_utils import get_superset_data

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI MinIO Service"}

@app.get("/minio-data")
async def fetch_minio_data():
    return get_minio_data()

@app.get("/superset-data")
async def fetch_superset_data():
    return get_superset_data()
