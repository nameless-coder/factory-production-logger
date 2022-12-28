import uvicorn
from fastapi import FastAPI

api = FastAPI(docs_url=None, redoc_url="/docs")


@api.get('/')
async def home():
    return {'message': 'Welcome to Factory Production Logger API!'}


if __name__ == '__main__':
    uvicorn.run("main:api", host="0.0.0.0", port=8080, reload=True)
