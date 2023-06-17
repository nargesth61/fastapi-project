from fastapi import FastAPI,status,Response,APIRouter , Query ,Body ,Path ,Depends
from enum import Enum
from pydantic import BaseModel
from typing import Annotated,List
from schemas import Userbase,Userdisplay,EmailRequest
from db.database import get_db
from db import user_db
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

router = APIRouter(prefix='/user', tags=['user'])



@router.post('/',response_model=Userdisplay)
def create_user(request:Userbase,db:Session=Depends(get_db)):
    return user_db.create_user(request,db)

