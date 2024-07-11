from fastapi.responses import Response
from fastapi import (
    APIRouter,
    status,
    HTTPException,
)
from user_app.services.user import UserService
from user_app.schemas.user import (
    CreateUserResponse,
    MultipleUsersResponse,
    User,
)


def create_user_router() -> APIRouter:

    user_router = APIRouter(
        prefix="/user",
        tags=["User EndPoints"],
    )
    user_service = UserService()

    @user_router.get("/alla", response_model=MultipleUsersResponse)
    async def get_multiple_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_service.get_multiple_users_with_pagination(start, limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users

    @user_router.get("/{user_id}", response_model=User)
    async def get_user_by_id(user_id: int = 0) -> dict:
        user = await user_service.get_user(user_id)
        return user

    @user_router.post("/", response_model=CreateUserResponse, status_code=201)
    async def add_user(new_user_info: User) -> CreateUserResponse:
        user_id = await user_service.create_or_update_user(new_user_info)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    @user_router.put("/{user_id}")
    async def update_user(user_id: int, user_details: User) -> None:
        await user_service.create_or_update_user(user_profile=user_details, new_user_id=user_id)
        return None

    @user_router.delete("/{user_id}")
    async def remove_user(user_id: int) -> None:
        try:
            await user_service.delete_user(user_id)
        except KeyError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} does not exist!"
            )

    @user_router.patch("/{user_id}", response_model=User)
    async def update_user_middle_name(user_id: int, middle_name: str) -> User:
        try:
            await user_service.update_middle_name(user_id, middle_name)
            updated_user = await user_service.get_user(user_id=user_id)
            return updated_user
        except KeyError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} does not exist!"
            )

    @user_router.patch("/dummy")
    async def test_response_code() -> Response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return user_router
