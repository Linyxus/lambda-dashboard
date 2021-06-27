from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.mount("/site", StaticFiles(directory="static", html = True), name="static")


@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}