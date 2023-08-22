
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Post
from app.schemas.post_schema import PostCreate as PostsCreateSchema
from app.utils.pagination import pagination


router = APIRouter()


@router.post("/")
async def create_post(post: PostsCreateSchema, db: Session = Depends(get_db)):
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


@router.get("/")
async def get_all_posts(
    pagination: tuple[int, int] = Depends(pagination),
    db: Session = Depends(get_db)):
    skip, limit = pagination
    posts = db.query(Post).offset(skip).limit(limit).all()
    if len(posts) <= 0:
        raise HTTPException(detail="No Post Exists", status_code=status.HTTP_404_NOT_FOUND)
    return {"data": posts}


@router.get("/{post_id}")
async def get_post_detail(post_id:int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(detail="Not-Found", status_code=status.HTTP_404_NOT_FOUND)
    return {"data": post}



@router.patch("/{post_id}")
async def update_post(post_id:int, post:PostsCreateSchema, db: Session = Depends(get_db)):
    post_query = db.query(Post).filter(Post.id == post_id)
    if post_query.first() == None:
        raise HTTPException(detail="Not-Found", status_code=status.HTTP_404_NOT_FOUND)
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    return {"data": post_query.first()}


@router.delete("/{post_id}")
async def delete_post(post_id:int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id)
    if post.first() is None:
        raise HTTPException(detail="Not-Found", status_code=status.HTTP_404_NOT_FOUND)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
