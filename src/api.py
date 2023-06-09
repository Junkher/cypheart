from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from service import get_load

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    question: str
    mode: str


@app.get("/")
async def root():
    return {"message": "Hello Idiot"}

@app.post("/item/")
async def create_item(item: Item):
    return item

@app.post("/chat/")
async def chat(item: Item):
    return get_load(item.question, item.mode)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, workers=1, log_level="info")