from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_root():
    return {"message": "server_up"}

