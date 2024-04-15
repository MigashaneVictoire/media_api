from fastapi import FastAPI
from fastapi.params import Body

######### creating the api (initial phase) ########
app = FastAPI()
 
# create web server with the bellow code
# terminal code: uvicorn main:app --reload

# Get request we are geeting importamtion from our api
@app.get("/")  #api decorator using a get http methode
def read_root():
    return {"Hello": "API's day three"}

@app.get("/post")
def get_post():
    return {"data":"This is the post"}


#Post request: We are sending impormation to the api
@app.post("/createpost")
def create_post(payload: dict = Body(...)): #extract the body from the post request
    print(payload)
    return {"new_post":f"title {payload['title']} and content {payload['content']}"}