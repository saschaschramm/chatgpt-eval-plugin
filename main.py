import builtins

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import Any

app: FastAPI = FastAPI(servers=[{"url": "http://localhost:8000"}])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/.well-known/", StaticFiles(directory=".well-known/"), name="static")

@app.get("/eval")
async def eval(string: str) -> dict:
    result: Any = builtins.eval(string)
    return {"result": str(result)}
