from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import zipfile
from typing import List
from generator import generate_embeddings
from response import run_query
import uvicorn
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str

app = FastAPI()

# Define directories for temporary storage, zipped file, and unzipped output
UPLOAD_DIR = "uploaded_files"
ZIP_OUTPUT_DIR = "zipped_output"
UNZIP_OUTPUT_DIR = "unzipped_output"

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(ZIP_OUTPUT_DIR, exist_ok=True)
os.makedirs(UNZIP_OUTPUT_DIR, exist_ok=True)

# Function to zip files
def zip_files(file_paths: List[str], zip_file_path: str):
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        for file_path in file_paths:
            zip_file.write(file_path, os.path.basename(file_path))

# Function to unzip files
def unzip_file(zip_file_path: str, unzip_dir: str):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall(unzip_dir)

def create_embeddings():
    zip_file_path = os.path.join(ZIP_OUTPUT_DIR, "uploaded_files.zip")

    # Check if the zip file exists
    if not os.path.exists(zip_file_path):
        return JSONResponse(content={"detail": "No zip file found to unzip"}, status_code=404)

    # Unzip the file into the unzip output directory
    unzip_file(zip_file_path, UNZIP_OUTPUT_DIR)

    # Loop through all the unzipped files and create embeddings
    unzipped_files = os.listdir(UNZIP_OUTPUT_DIR)
    if not unzipped_files:
        return JSONResponse(content={"detail": "No files found to create embeddings"}, status_code=404)

    embeddings = generate_embeddings(path=UNZIP_OUTPUT_DIR)

    return JSONResponse(content={"detail": "Embeddings created successfully", "success": True})

@app.post("/upload-files/")
async def upload_files(files: List[UploadFile] = File(...)):
    saved_file_paths = []
    
    try:
        # Save the uploaded files to the upload directory
        for file in files:
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            saved_file_paths.append(file_path)
            with open(file_path, "wb") as f:
                f.write(await file.read())

        # Zip the files and store them in the zip output directory
        zip_file_path = os.path.join(ZIP_OUTPUT_DIR, "uploaded_files.zip")
        zip_files(saved_file_paths, zip_file_path)

        # Automatically run create_embeddings after upload completes
        embeddings_response = create_embeddings()

        # Combine both upload and embedding responses
        return JSONResponse(content={
            "detail": "Files uploaded, zipped, and embeddings created successfully",
            "success": True
        })

    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=500)

@app.post("/get-response/")
async def get_response(query: str):
    try:
        run_query(query)
        return JSONResponse(content={"detail":"Query executed successfully", "success": True})
    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=500)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running..."}


if __name__ == "__main__":
    # Run the FastAPI app
    uvicorn.run(app, host="127.0.0.1", port=8000)
