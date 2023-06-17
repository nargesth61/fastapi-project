from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Sequence
from sqlalchemy.orm import relationship
from db.database import Base


class User(Base):
    __tablename__ ="user"
    
    id = Column(Integer, index=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String,unique=True)
    items = relationship("Post",back_populates='user')


class Post(Base):
    __tablename__ = "post"
    
    id = Column(Integer, index=True, primary_key=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship("User",back_populates='items')

'''
هنوز تکمیل نشده
'''
class Otp(Base):
    __tablename__ = "otp",
    
    id= Column('id', Integer, Sequence('otp_id_seq'), primary_key=True),
    recipient_id=Column('recipient_id', String(100)),
    session_id=Column('session_id', String(100)),
    otp_code=Column('otp_code', String(6)),
    status=Column('status', String(1)),
    created_on=Column('created_on', DateTime),
    updated_on=Column('updated_on', DateTime),
    otp_failed_count=Column('otp_failed_count', Integer, default=0),

class OtpBlocks(Base):
    __tablename__ = "otpBlocks",
    
    id=Column('id', Integer, Sequence('otp_block_id_seq'), primary_key=True),
    recipient_id= Column('recipient_id', String(100)),
    session_id=Column('session_id', String(100)),
    created_on= Column('created_on', DateTime),
