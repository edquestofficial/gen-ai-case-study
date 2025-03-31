from fastapi import FastAPI
from datetime import datetime

#pip install fastapi uvicorn

# Initialize the FastAPI app
app = FastAPI()

# Define a route to return "Hello edquest" with the current timestamp
@app.get("/")
def read_root():
    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": f"Hello Edquest\n", "timestamp": current_time}

# Define another route with a parameter
@app.get("/greet/{name}")
def greet(name: str):
    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": f"Hello, {name}!", "timestamp": current_time}

# Define a POST route
@app.post("/items/")
def create_item(item: dict):
    return {"message": "Item created", "item": item}
