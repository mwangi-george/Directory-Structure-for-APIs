from fastapi import APIRouter
from app.services.user import UserService
from app.schemas.user import (
    CreateUserResponse,
    MultipleUsersResponse,
    User,
)


def create_user_router() -> APIRouter:

    user_router = APIRouter()
    user_service = UserService()

    @user_router.get("/user/{user_id}", response_model=User)
    async def get_user_by_id(user_id: int = 0) -> dict:
        user = await user_service.get_user(user_id)
        print(f"The docstring of get_user function is {
            user_service.get_user.__doc__}")
        return user

    @user_router.post("/users", response_model=CreateUserResponse)
    async def add_user(new_user_info: User):
        user_id = await user_service.create_or_update_user(new_user_info)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    @user_router.get("/users", response_model=MultipleUsersResponse)
    async def get_multiple_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_service.get_multiple_users_with_pagination(start, limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users

    @user_router.put("/user/{user_id}")
    async def update_user(user_id: int, user_profile: User) -> None:
        await user_service.create_or_update_user(user_profile, user_id)
        return None

    @user_router.delete("/user/{user_id}")
    async def remove_user(user_id: int) -> None:
        await user_service.delete_user(user_id)
        return None

    @user_router.patch("/user/{user_id}", response_model=User)
    async def update_user_middle_name(user_id: int, middle_name: str) -> User:
        await user_service.update_middle_name(user_id, middle_name)
        updated_user = await user_service.get_user(user_id=user_id)
        return updated_user

    return user_router
