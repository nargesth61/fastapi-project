from pydantic import BaseModel
from datetime import datetime
from typing import List

'''
Functions that have display at theend of their
names are used to display information to the user in response
'''


class Userbase(BaseModel):
    username: str
    email: str
    password: str


class Userdisplay(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int



class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User

    class Config:
        orm_mode = True

class Userauth(BaseModel):
    id :int
    username :str
    email:str
    class Config:
        orm_mode = True


'''
این قسمت هنوز تکمیل نشده استاد
'''
class EmailRequest(BaseModel):
    email: str


class CreateOTP(BaseModel):
    recipient_id: str


class VerifyOTP(CreateOTP):
    session_id: str
    otp_code: str
