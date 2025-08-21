from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from .. database import get_db
from routers.auth_utils import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["profile"]

)

@router.get("/{username}")
def get_user_profile(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "bio": user.bio,
        "profile_picture_url": user.profile_picture_url,
        "location": user.location,
        "links": user.links 
    }
    @router.put("/")
    def update_user_profile(
        bio: str= None,
        location: str = None,
        links: str = None,
        profile_picture_url: str = None,
        db: Session = Depends(database.get_db),
        current_user: models.User = Depends(get_current_user)
    ):
        if bio is not None:
            current_user.bio = bio
        if location is not None:
            current_user.location = location
        if links is not None:
            current_user.links = links
        if profile_picture_url is not None:
            current_user.profile_picture_url = profile_picture_url
            db.commit()
            db.refresh(current_user)
            return{message:"Profile updated successfully", "user":current_user}
        
        