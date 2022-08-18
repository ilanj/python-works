import os
import pickle
import numpy as np
import joblib
import logging

# FastAPI imports
from fastapi import FastAPI, Request
# uvicorn
import uvicorn
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# load model
vectorizer = joblib.load("model/vectorizer")
model = joblib.load("model/nb_model.h5")
with open('model/classes.pkl', 'rb') as fptr:
    class_names = pickle.load(fptr)
properties = None


class RequestModel(BaseModel):
    request_string: List[str] = None


@app.post("/classify")
async def root(request_model: RequestModel):
    '''

    :param request_model: list of string (can view from swagger)
    :return: class type, conf score
    '''
    prob = model.predict_proba(vectorizer.transform(request_model.request_string))
    max_prob_class_index = np.argmax(prob, axis=1)
    results = ([{"cls": class_names[int(doc_class)], "conf": prob[index][doc_class]} for index, doc_class in
                enumerate(max_prob_class_index)]
    )
    return results


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")