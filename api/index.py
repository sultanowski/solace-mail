from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("auth.router:app", host="0.0.0.0", log_level="info")
