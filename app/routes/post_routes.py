from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_db
from app.models import Posts
from app.utils.pagination import pagination
from app.services.auth_services import get_current_user

router = APIRouter(prefix="/posts", tags=["POSTS"])


@router.post("/", response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(get_current_user)
    ):
    new_post = Posts(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/", response_model=list[schemas.Post])
async def get_all_posts(
    pagination: tuple[int, int] = Depends(pagination), 
    db: Session = Depends(get_db)
):
    skip, limit = pagination
    posts = db.query(Posts).offset(skip).limit(limit).all()
    if len(posts) <= 0:
        raise HTTPException(
            detail="No Post Exists", status_code=status.HTTP_404_NOT_FOUND
        )
    return posts


@router.get("/{post_id}", response_model=schemas.Post)
async def get_post_detail(
    post_id: int, 
    db: Session = Depends(get_db)
    ):
    post = db.query(Posts).filter(Posts.id == post_id).first()
    if not post:
        raise HTTPException(detail="Not-Found", status_code=status.HTTP_404_NOT_FOUND)
    return post


@router.patch("/{post_id}", response_model=schemas.Post)
async def update_post(
    post_id: int, 
    post: schemas.PostCreate, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(get_current_user)
):
    post_query = db.query(Posts).filter(Posts.id == post_id)
    if post_query.first() == None:
        raise HTTPException(detail="Not-Found", status_code=status.HTTP_404_NOT_FOUND)
    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()


@router.delete("/{post_id}")
async def delete_post(
    post_id: int, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(get_current_user)
    ):
    post = db.query(Posts).filter(Posts.id == post_id)
    if post.first() is None:
        raise HTTPException(detail="Not-Found", status_code=status.HTTP_404_NOT_FOUND)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
