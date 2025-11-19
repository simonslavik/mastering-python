from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-word")

def hello_world():
    return {"message": "Hello, World!"}

