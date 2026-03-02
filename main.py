from fastapi import FastAPI

app = FastAPI() # uvicorn main:app --reload

from routes.order_routes import order_router

app.include_router(order_router)