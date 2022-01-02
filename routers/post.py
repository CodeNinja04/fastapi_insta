from fastapi import APIRouter, Depends,HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from routers.schemas import PostBase, PostDisplay, UserDisplay
from db import db_post
from typing import List

router = APIRouter(
    prefix='/post',
    tags=['post']
)

image_url_types=['absolute', 'relative']

@router.post('',response_model=PostDisplay)
def create(request:PostBase,db:Session=Depends(get_db) ):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail='image type not supported')
    return db_post.create(db,request)

@router.get('',response_model=List[PostDisplay])
def posts(db:Session=Depends(get_db)):
    return db_post.get_all(db)
    