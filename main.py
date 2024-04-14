from fastapi import FastAPI

######### creating the api (initial phase) ########
app = FastAPI()

# create web server with the bellow code
# terminal code: uvicorn main:app --reload
@app.get("/")  #api decorator using a get http methode
def read_root():
    return {"Hello": "My first api creation"}