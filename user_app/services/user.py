from typing import Optional, Tuple
from user_app.schemas.user import User


class UserService:
    """A class putting all the functions about users together"""

    def __init__(self) -> None:
        pass

    all_users = {
        0: {
            "first_name": "George",
            "middle_name": "Ngugi",
            "last_name": "Mwangi"
        }
    }

    async def create_or_update_user(self, user_profile: User, new_user_id: Optional[int] = None) -> int:
        if new_user_id is None:
            new_user_id = len(self.all_users)

        self.all_users[new_user_id] = {
            "first_name": user_profile.first_name,
            "middle_name": user_profile.middle_name,
            "last_name":  user_profile.last_name
        }

        return new_user_id

    async def get_user(self, user_id: int = 0) -> User:
        user = self.all_users[user_id]
        return User(**user)

    async def get_multiple_users_with_pagination(self, start: int, limit: int) -> Tuple[list[User], int]:
        """Get 2 users at a time"""

        list_of_users = []
        keys = list(self.all_users.keys())
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

    async def delete_user(self, user_id: int) -> None:
        del self.all_users[user_id]

    async def update_middle_name(self, user_id: int, middle_name: str) -> None:
        self.all_users[user_id]["middle_name"] = middle_name
        return None
