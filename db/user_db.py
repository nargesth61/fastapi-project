from db.models import User
from schemas import Userbase
from sqlalchemy.orm.session import Session
from db.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status

'''
create new user in database and register
'''
def create_user(request:Userbase,db:Session):
    user = User(
        username = request.username,
        password =Hash.bcrypt(request.password),
        email = request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)


def get_user_by_username(username:str , db:Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    return user
