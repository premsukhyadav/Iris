from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import pickle
import numpy as np
import os

# Class labels mapping
CLASS_NAMES = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

# Load the saved model
MODEL_PATH = "model/model.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Mount templates
templates = Jinja2Templates(directory="templates")

# Serve homepage
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...)
):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    predicted_class = model.predict(data)[0]
    predicted_name = CLASS_NAMES.get(predicted_class, "Unknown")
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": predicted_name}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
