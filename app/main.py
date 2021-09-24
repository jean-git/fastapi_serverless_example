import os
from fastapi import FastAPI
from mangum import Mangum
from app.api.api_v1.api import router as api_router

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

#app = FastAPI(title="MyAwesomeApp")
app = FastAPI(title="MyAwesomeApp", openapi_prefix=openapi_prefix)

@app.get("/")
def hello_world():
    return {"message": "Hello World!!!"}

app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)