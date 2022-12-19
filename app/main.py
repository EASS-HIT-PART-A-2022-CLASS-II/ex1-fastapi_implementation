from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"message_get":"Success!"}


@app.post("post")
def post_root():
        return {"message":"hello world","method":"POST"}