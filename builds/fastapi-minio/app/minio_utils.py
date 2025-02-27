from minio import Minio

MINIO_URL = "minio:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"

client = Minio(MINIO_URL, access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY, secure=False)

def get_minio_data():
    buckets = client.list_buckets()
    return {"buckets": [bucket.name for bucket in buckets]}
