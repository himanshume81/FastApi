from typing import Literal

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    phone_number: str | None = None
    status: Literal["active", "inactive"]
    role: Literal["admin", "user"]


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    status: Literal["active", "inactive"] | None = None
    role: Literal["admin", "user"] | None = None


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
