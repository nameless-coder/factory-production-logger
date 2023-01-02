from fastapi import FastAPI, status
from database.connection import Settings

from routes.production_run import production_run_router

import uvicorn

api = FastAPI(docs_url="/swagger", redoc_url="/docs")

settings = Settings()

api.include_router(production_run_router, prefix="/productionrun")


@api.on_event("startup")
async def init_db():
    await settings.initialize_database()


@api.get('/',
         response_description="Welcome page",
         status_code=status.HTTP_200_OK,
         tags=["Home"])
async def home() -> dict:
    return {
        'message': 'Welcome to Factory Production Logger API!'
    }


if __name__ == '__main__':
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
