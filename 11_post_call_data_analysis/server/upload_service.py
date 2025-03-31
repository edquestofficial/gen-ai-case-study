import os

UPLOAD_DIR = "uploads"

class UploadService:
    def __init__(self):
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)

    def upload_book(self, file, chapter_name, class_type, subject):
        try:
            folder_path = os.path.join(UPLOAD_DIR, class_type, subject)
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, f"{chapter_name}.pdf")
            with open(file_path, "wb") as f:
                f.write(file.read())
            return {"path": file_path}, 201
        except Exception as e:
            return {"error": str(e)}, 500
