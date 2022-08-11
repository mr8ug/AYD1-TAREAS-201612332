from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/add/")
async def add(request: Request, x: int, y: int):
    return x + y


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=3000)