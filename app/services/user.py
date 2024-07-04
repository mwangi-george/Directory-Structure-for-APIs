

def get_road_info(road_id) -> Roads:
    all_roads = {
        1: {
            "road_id": 1,
            "road_name": "Thika Super Highway",
            "lanes": 10,
            "origin": "Nairobi City",
            "destination": "Thika Town"
        },
        2: {
            "road_id": 2,
            "road_name": "Nairobi-Nakuru Highway",
            "lanes": 4,
            "origin": "Nairobi City",
            "destination": "Nakuru Town"
        },
        3: {
            "road_id": 3,
            "road_name": "Mombasa Road",
            "lanes": 6,
            "origin": "Nairobi City",
            "destination": "Mombasa Town"
        },
        4: {
            "road_id": 4,
            "road_name": "Ngong Road",
            "lanes": 2,
            "origin": "Nairobi City",
            "destination": "Ngong Town"
        },
        5: {
            "road_id": 5,
            "road_name": "Mundoro - Kiganjo - Kimbo",
            "lanes": 2,
            "origin": "Mundoro Town",
            "destination": "Kimbo"
        }
    }

    # Subset dictionary to get details for a specified road
    road_details = all_roads[road_id]
    return Roads(**road_details)


# Using a list of dictionaries for easier subsetting
# defining it globally for later use
all_users = {
    0: {
        "first_name": "George",
        "middle_name": "Ngugi",
        "last_name": "Mwangi"
    }
}


def get_user(user_id: int = 0) -> User:
    """
    Function to get a user's information by id 

    :param user_id: int - Unique monotonically increasing integer id
    :return: User object
    """

    # The docstring can be accessed by calling get_user.__doc__
    user = all_users[user_id]
    return User(**user)


def create_or_update_user(user_profile: User, new_user_id: Optional[int] = None) -> int:
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


def get_multiple_users_with_pagination(start: int, limit: int) -> Tuple[list[User], int]:
    """Get 2 users at a time"""

    list_of_users = []  # start with an empty list of users

    keys = list(all_users.keys())  # get all keys in the all_users dictionary
    total = len(keys)
    # loop over the keys
    for index in range(0, len(keys), 1):
        if index < start:
            continue

        current_key = keys[index]
        user = get_user(current_key)
        list_of_users.append(user)

        if len(list_of_users) >= limit:
            break

    return list_of_users, total


# a function to perform deletion
def delete_user(user_id: int) -> None:
    # add error handling for key not found
    del all_users[user_id]  # just deleting the keys


def update_middle_name(user_id: int, middle_name: str) -> None:
    all_users[user_id]["middle_name"] = middle_name
    return None
