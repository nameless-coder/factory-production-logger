import uvicorn
from fastapi import FastAPI

from item import item_router

api = FastAPI(docs_url=None, redoc_url="/docs")


@api.get('/')
async def home() -> dict:
    return {
        'message': 'Welcome to Factory Production Logger API!'
    }


api.include_router(item_router)


if __name__ == '__main__':
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
