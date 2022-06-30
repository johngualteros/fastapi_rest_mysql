from fastapi import FastAPI
from routes.user import user
app=FastAPI(
    title="FastAPI",
    description="FastAPI is a Python framework for building blazing fast APIs.",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    openapi_tags=[{
        "name": "users",
        "description": "Users API"
    }]
)
app.include_router(user)