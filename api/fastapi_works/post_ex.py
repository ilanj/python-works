import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RequestModel(BaseModel):
    no: int


class ResponseModel(BaseModel):
    res: int


@app.post("/get_sq")
async def get_sq(req: RequestModel):

    return {req.no: req.no * req.no}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
