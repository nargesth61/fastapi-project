from fastapi import FastAPI,status,Response,APIRouter ,Depends,UploadFile, File
from pydantic import BaseModel
from typing import Annotated,List
from schemas import PostBase,PostDisplay,Userauth
from db.database import get_db
from db import post_db
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from typing import List
import random
import shutil
from string import ascii_letters
from auth.oauth2 import get_curent_tokens



router = APIRouter(prefix='/post', tags=['post'])


image_url_tyopes = ["url", "uploaded"]

'''
for create new post and get user id for post
'''
@router.post('/',response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db),
                curent_user:Userauth=Depends(get_curent_tokens)):
    if request.image_url_type not in image_url_tyopes:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail="image url type should be 'url' or 'uploaded'")
    return post_db.create_post(request, db)

'''
Only the user who created the post can delete it
'''
@router.post('/delete/{id}')
def delete_post(id:int, db: Session = Depends(get_db),
                curent_user:Userauth=Depends(get_curent_tokens)):
    return post_db.delete_post(id=id,db=db,user_id=curent_user.id)

@router.get('/posts',response_model=List[PostDisplay])
def get_all_posts(db:Session=Depends(get_db)):
    return post_db.get_all_post(db)


@router.post('/upload_file')
def upload_file(file: UploadFile = File(...)):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit('.', 1))
    path_file = f"uploaded_files/{new_name}"
    with open(path_file, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"path_file": path_file}