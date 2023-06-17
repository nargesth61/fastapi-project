from db.database import engine
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from fastapi import FastAPI,status,Response
from db.models import Base
from router import user
from router import post
from fastapi.staticfiles import StaticFiles
from auth import authentication



app = FastAPI()


Base.metadata.create_all(engine)
'''
برای زمانی که نیاز داریم دو برنامه به صورت مستقل و رابط کاربری اسناد خودمون داشته باشیم
 استفادت میکنیم mount از 
'''
app.mount("/uploaded_files", StaticFiles(directory="uploaded_files"), name="uploaded_files")

app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)