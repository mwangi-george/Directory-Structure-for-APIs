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

    async def get_user(user_id: int = 0) -> User:
        """
        Function to get a user's information by id 

        :param user_id: int - Unique monotonically increasing integer id
        :return: User object
        """

        # The docstring can be accessed by calling get_user.__doc__
        user = all_users[user_id]
        return User(**user)

    async def create_or_update_user(user_profile: User, new_user_id: Optional[int] = None) -> int:
        # Get the data using User
        # since the keys start from 0, length will be 1
        if new_user_id is None:
            new_user_id = len(all_users)

        print("Before")
        print(all_users)
        # add new user to dictionary using keys
        all_users[new_user_id] = {
            "first_name": user_profile.first_name,
            "middle_name": user_profile.middle_name,
            "last_name":  user_profile.last_name
        }

        print("After")
        print(all_users)

        return new_user_id

    # functions to get multiple users

    async def get_multiple_users_with_pagination(start: int, limit: int) -> Tuple[list[User], int]:
        """Get 2 users at a time"""

        list_of_users = []  # start with an empty list of users

        # get all keys in the all_users dictionary
        keys = list(all_users.keys())
        total = len(keys)
        # loop over the keys
        for index in range(0, len(keys), 1):
            if index < start:
                continue

            current_key = keys[index]
            user = await get_user(current_key)
            list_of_users.append(user)

            if len(list_of_users) >= limit:
                break

        return list_of_users, total

    # a function to perform deletion

    async def delete_user(user_id: int) -> None:
        # add error handling for key not found
        del all_users[user_id]  # just deleting the keys

    async def update_middle_name(user_id: int, middle_name: str) -> None:
        all_users[user_id]["middle_name"] = middle_name
        return None
