from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "hola mundo"

@app.get("/url")
async def url():
    return {
        "Nombre": "Joseph trujillo",
        "user_id": "https://moure.dev"
    }