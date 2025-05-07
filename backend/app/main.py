
from fastapi import FastAPI
from app.api import products

app = FastAPI(title="CMS API")

app.include_router(products.router, prefix="/products")
