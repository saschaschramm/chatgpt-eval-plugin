import builtins
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

app = FastAPI(servers=[{"url": "http://localhost:8000"}])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/.well-known/ai-plugin.json")
async def ai_plugin():
    with open(os.path.join(".well-known", "ai-plugin.json"), mode="r") as f:
        text = f.read()
    return Response(text, media_type="application/json")


@app.get("/logo.svg")
async def logo():
    with open(os.path.join("logo.svg"), mode="rb") as f:
        image = f.read()
    return Response(image, media_type="image/svg+xml")


@app.get("/eval")
async def eval(string: str):
    result = builtins.eval(string)
    return {"result": result}
