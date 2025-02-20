from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from api import router as youtube

app = FastAPI()

origins = ["localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(youtube, prefix="/api")

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Hello World!"})


