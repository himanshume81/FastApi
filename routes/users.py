from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas.user import UserCreate, UserResponse, UserUpdate
from services.user_service import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)

router = APIRouter()


@router.post("/users", response_model=UserResponse, status_code=201)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/users", response_model=list[UserResponse])
def list_users_route(db: Session = Depends(get_db)):
    return get_users(db)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.put("/users/{user_id}", response_model=UserResponse)
def replace_user_route(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(
        db,
        user_id,
        UserUpdate(
            name=user.name,
            email=user.email,
            phone_number=user.phone_number,
            status=user.status,
            role=user.role,
        ),
    )

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user


@router.delete("/users/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}


@router.patch("/users/{user_id}", response_model=UserResponse)
def patch_user_route(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = update_user(db, user_id, data)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.get("/userupdate")
def get_user_update(
    city: list[str] = Query(default=[]),
    age: int | None = None,
):
    return {
        "cities": city,
        "age": age,
    }