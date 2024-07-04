from typing import Optional
from pydantic import (
    BaseModel,
    Field,
)


class User(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str

    # Attributes Configurations
    class Config:
        str_max_length = 30
        str_min_length = 2

# a simple model to store the returned id


class CreateUserResponse(BaseModel):
    user_id: int


class MultipleUsersResponse(BaseModel):
    """Every element in the users list is going to be of class User"""
    users: list[User]
    total: int
