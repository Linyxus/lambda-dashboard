from typing import Optional
import json

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import aioredis


async def redis_conn():
    return await aioredis.create_redis('redis://localhost:6379')


app = FastAPI()


app.mount("/site", StaticFiles(directory="static", html = True), name="static")


@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.get("/api/hot_genres")
async def get_hot_genres():
    redis = await redis_conn()
    res = await redis.lrange('vis_hot_genres', 0, -1)
    res = [json.loads(x) for x in res]
    return res


@app.get("/api/top_genres")
async def get_top_genres():
    redis = await redis_conn()
    res = await redis.lrange('vis_top_genres', 0, -1)
    res = [json.loads(x) for x in res]
    return res


@app.get("/api/hot_films")
async def get_hot_genres():
    redis = await redis_conn()
    res = await redis.lrange('vis_hot_films', 0, -1)
    res = [json.loads(x) for x in res]
    return res


@app.get("/api/top_films")
async def get_top_genres():
    redis = await redis_conn()
    res = await redis.lrange('vis_top_films', 0, -1)
    res = [json.loads(x) for x in res]
    return res
