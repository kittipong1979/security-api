from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Running ✅"}

@app.get("/check")
def check(product: str):
    return {
        "product": product,
        "status": "working ✅"
    }
