from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware







app= FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow only specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def welcome():
    return Response(content="Welcome to home page")

from controller.user_controller import router

app.include_router(router)






