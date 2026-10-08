from sqlalchemy import Column, Enum, Integer, String
from database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    status = Column(
        Enum("active", "inactive", name="user_status_enum"),
        nullable=False,
    )
    role = Column(
        Enum("admin", "user", name="user_role_enum"),
        nullable=False,
    )
