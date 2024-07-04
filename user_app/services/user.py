from typing import Optional, Tuple
from user_app.schemas.user import User

# Using a list of dictionaries for easier subsetting
# defining it globally for later use
all_users = {
    0: {
        "first_name": "George",
        "middle_name": "Ngugi",
        "last_name": "Mwangi"
    }
}


class UserService:
    """A class putting all the functions about users together"""

    def __init__(self) -> None:
        pass

    async def create_or_update_user(user_profile: User, new_user_id: Optional[int] = None) -> int:
        if new_user_id is None:
            new_user_id = len(all_users)

        all_users[new_user_id] = {
            "first_name": user_profile.first_name,
            "middle_name": user_profile.middle_name,
            "last_name":  user_profile.last_name
        }

        return new_user_id

    @staticmethod
    async def get_user(user_id: int = 0) -> User:
        user = all_users[user_id]
        return User(**user)

    async def get_multiple_users_with_pagination(self, start: int, limit: int) -> Tuple[list[User], int]:
        """Get 2 users at a time"""

        list_of_users = []
        keys = list(all_users.keys())
        total = len(keys)

        for index in range(0, len(keys), 1):
            if index < start:
                continue

            current_key = keys[index]
            user = await self.get_user(current_key)
            list_of_users.append(user)

            if len(list_of_users) >= limit:
                break

        return list_of_users, total

    @staticmethod
    async def delete_user(user_id: int) -> None:
        del all_users[user_id]

    @staticmethod
    async def update_middle_name(user_id: int, middle_name: str) -> None:
        all_users[user_id]["middle_name"] = middle_name
        return None
