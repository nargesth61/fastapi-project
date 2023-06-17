from fastapi import FastAPI,status,Response,APIRouter , Query ,Body ,Path ,Depends
from typing import Annotated,List
from db.database import get_db
from db import models,hash
from db.hash import Hash
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from auth.oauth2 import create_access_token
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db import models
from db.database import get_db
from db.hash import Hash
from auth import oauth2
from db.models import User
from schemas import EmailRequest
import uuid


router = APIRouter(tags=['authentication'])

'''
create token for user aftet register and login for
acsess
'''
@router.post('/token')
def get_token(request:OAuth2PasswordRequestForm=Depends(),db :Session=Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(detail='not found',status_code=status.HTTP_404_NOT_FOUND)
    if not Hash.verify(user.password, request.password):
         raise HTTPException(detail='wrong pass',status_code=status.HTTP_404_NOT_FOUND)
    access_token=create_access_token(data={'sub':user.username})
    return {
        'access_token':access_token,
        'type_token':'Bearer',
        'user': user.id
    }

