'''
send req from postman using http://localhost:5000/items/ddd/dd?q1=test1&q2=test2
'''
from typing import Optional, List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import RedirectResponse

tags_metadata = [
    {
        "name": "Topic 1",
        "description": "_Start/Stop/Poll_ the **model training**.",
    },
    {
        "name": "Healthcheck",
        "description": "Check if the **trainer service is up and running**.",
    }
]

# Fast API wrapper
app = FastAPI(
    title="fastapi with pydantic model",
    description="fatsapi pydantic swagger tutorical",
    docs_url="/swagger",
    openapi_tags=tags_metadata,
)

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    nos: List[int] = []

@app.get("/items/{item_id}/{test}")
async def read_item(item_id: str, test: str, q1: Optional[str] = None, q2: Optional[str] = None):
    if q1 and q2:
        return {"item_id": item_id, "test": test, "q1": q1, "q2" : q2}
    return {"item_id": item_id, "test": test}

@app.get("/")
async def root():
    return RedirectResponse("/swagger")

@app.get("/ex")
async def read_item():
    return "hello world"

<<<<<<< HEAD
@app.post("/postex/")
async def create_item(item: Item):
    return item

=======
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
@app.post("/status/")
async def create_item(item: Item):
    #update in DB and UI
    return {"status" : "Received"}
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, log_level="info")