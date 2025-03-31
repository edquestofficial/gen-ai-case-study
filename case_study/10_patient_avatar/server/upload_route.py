from fastapi import APIRouter, UploadFile, Form, File, HTTPException
from upload_service import UploadService
from data_insertion import insert_data

upload_service = UploadService()

router = APIRouter()

@router.post("/upload")
async def upload_book(
    file: UploadFile = File(...),
    chapter_name: str = Form(...),
    class_type: int = Form(...),
    subject: str = Form(...)
):
    if not file or not chapter_name or not class_type or not subject:
        raise HTTPException(status_code=400, detail="Missing required fields")

    class_type_str = str(class_type)

    response, status_code = upload_service.upload_book(
        file.file, chapter_name, class_type_str, subject
    )
    if status_code != 201:
        raise HTTPException(status_code=status_code, detail=response["error"])
    print({"message": "File uploaded successfully", "path": response["path"]})
    return insert_data(response["path"], chapter_name, class_type, subject)

