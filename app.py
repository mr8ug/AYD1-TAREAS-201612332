from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/add/")
async def add(request: Request, x: int, y: int):
    return x + y

@app.get("/info")
async def info():
    return {"info":{"nombre": "Carlos Emilio Campos Moran","carnet":201612332}}

@app.post("/sub/")
async def sub(request: Request, x: int, y: int):
    return x - y

@app.post("/mul/")
async def sub(request: Request, x: int, y: int):
    return x * y

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=3000)