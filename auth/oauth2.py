from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI,status,Response,APIRouter , Query ,Body ,Path ,Depends
from typing import Annotated,List,Optional
from db.database import get_db
from db import user_db,post_db
from datetime import timedelta ,datetime
from jose import  jwt
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from jose.exceptions import JWTError 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '6c7d438d2ea66cc11ee315566bda6f45336930dc2a40eaa96ec009524c20aa69'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30




'''
Token creation for user access and login
'''
def create_access_token(data:dict,expire_dalate:Optional[timedelta]=None):
    to_encode=data.copy()
    if expire_dalate:
        expire = datetime.utcnow()+expire_dalate
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp':expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt




"""
Receiving the username from the user and checking the 
user's username in token and checking the user's register
"""
def get_curent_tokens(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='wrong token',
                          headers={'WWW-authenticate':'bearer'}
                           )
    try:
        dic = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        username = dic.get('sub')
        if not username :
            raise error
    except JWTError:
       raise error
    
    user =user_db.get_user_by_username(username,db)
    return user

