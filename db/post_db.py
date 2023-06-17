from db.models import Post
from schemas import PostBase
from sqlalchemy.orm.session import Session
from db.hash import Hash
import datetime
from fastapi.exceptions import HTTPException
from fastapi import status


'''
for create a new post by user and save that post in database
'''
def create_post(request:PostBase,db:Session):
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

'''
for delete post by the user who created this post
'''
def delete_post(id:int,db:Session,user_id:int):
    post = db.query(Post).filter(Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    db.delete(post)
    db.commit()
    return 'Ok'

'''
show all posts in database
'''
def get_all_post(db:Session):
    return db.query(Post).all()


