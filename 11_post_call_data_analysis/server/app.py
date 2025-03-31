from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tutor_route import router as tutor_router
from upload_route import router as upload_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tutor_router, prefix="/tutor")
app.include_router(upload_router)

@app.get("/")
async def get():
    return {"message": "hiii"}
