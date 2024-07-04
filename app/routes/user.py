from fastapi import APIRouter


user_router = APIRouter()


@user_router.get("/user/{user_id}", response_model=User)
def get_user_by_id(user_id: int = 0) -> dict:
    user = await get_user(user_id)
    print(f"The docstring of get_user function is {get_user.__doc__}")
    return user


@user_router.post("/users", response_model=CreateUserResponse)
def add_user(new_user_info: User):
    user_id = await create_or_update_user(new_user_info)
    created_user = CreateUserResponse(user_id=user_id)
    return created_user


@user_router.get("/users", response_model=MultipleUsersResponse)
def get_multiple_users_paginated(start: int = 0, limit: int = 2):
    users, total = await get_multiple_users_with_pagination(start, limit)
    formatted_users = MultipleUsersResponse(users=users, total=total)
    return formatted_users


@user_router.put("/user/{user_id}")
def update_user(user_id: int, user_profile: User) -> None:
    await create_or_update_user(user_profile, user_id)
    return None


@user_router.delete("/user/{user_id}")
def remove_user(user_id: int) -> None:
    await delete_user(user_id)
    return None


@user_router.patch("/user/{user_id}", response_model=User)
def update_user_middle_name(user_id: int, middle_name: str) -> User:
    await update_middle_name(user_id, middle_name)
    return await get_user(user_id=user_id)
