import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models
from . import schemas
from .routers import users, appointments, prescriptions, messages

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(users.router)
app.include_router(appointments.router)
app.include_router(prescriptions.router)
app.include_router(messages.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/health')
def health_check():
    return {'status': 'ok'}

@app.exception_handler(Exception)
def unicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={'detail': f'An unexpected error occurred: {str(exc)}'})

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{{"file_path:path}}")
    async def serve_frontend(file_path: str):
        if file_path.startswith("api/") or file_path == "":
            return None  # Let API routes handle it
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")  # SPA routing


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
