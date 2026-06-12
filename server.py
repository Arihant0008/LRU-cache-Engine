from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from phase1 import LRUCache

app = FastAPI()

my_cache = LRUCache(3)

class CacheItem(BaseModel):
    key : int
    value : str

@app.get("/get/{key}")
def get_from_cache(key : int):
    result = my_cache.get(key)
    if result == -1:
        raise HTTPException(status_code = 404, detail= "Key not found")

    return {"key": key, "value": result}

@app.post("/put")
def put_in_cache(item: CacheItem):
    my_cache.put(item.key, item.value) 
    return {"message" : f"Successfully cached {item.key}"}
