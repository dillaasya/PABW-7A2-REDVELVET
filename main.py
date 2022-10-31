from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return 'Hello World, by PABW 7A2 REDVELVET'